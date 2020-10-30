NULL = '\\N'


class Buf:
    def __init__(self, storage, size):
        self.storage = storage
        self.buf = ''
        self.size = size
        self.counter = 0

    def write(self, text):
        self.counter += 1
        self.buf += text
        if self.counter > self.size:
            self.clear()

    def clear(self):
        self.storage.write(self.buf)
        self.buf = ''
        self.counter = 0


class Table:
    out = 'out'
    tables = []

    def __init__(self, name, fields, out=False):
        self.name = name
        self.fields = fields
        if out:
            self.out = out
        self.storage = open(f'{self.out}/{name}.tsv', 'w', encoding='utf-8', newline='')
        self.active = True
        self.counter = 0
        self.skip = 1000000
        self.auto_increment = {}
        self.storage.write(Table.join(self.fields) + '\n')
        self.buf = Buf(self.storage, 5000)
        Table.tables.append(self)

    def close(self):
        self.buf.clear()
        self.storage.close()
        self.active = False

    def insert(self, item):
        if self.active:
            for auto_field in self.auto_increment:
                if auto_field not in item:
                    self.auto_increment[auto_field] += 1
                    item[auto_field] = self.auto_increment[auto_field]
            aov = [str(item.get(f, '')) for f in self.fields]
            self.buf.write(Table.join(aov) + '\n')
            self.counter += 1
            if self.counter % self.skip == 0:
                print(f'Write {self.counter} rows to table {self.name}')
            return item
        else:
            raise Exception('Table is closed')

    def insert_arr(self, item, arr_field, arr):
        for el in arr:
            item[arr_field] = el
            self.insert(item)

    @staticmethod
    def join(arr):
        return '\t'.join(arr)

    @staticmethod
    def close_all():
        for tab in Table.tables:
            tab.close()


class Dictionary(Table):
    def __init__(self, name, fields):
        if len(fields) != 2:
            raise Exception('Dictionary must have 2 fields!')
        super().__init__(name, fields)
        self.dict_id = 0
        self.dict_index = {}

    def add(self, el):
        if el == NULL:
            return NULL
        if el not in self.dict_index:
            self.dict_id += 1
            self.dict_index[el] = self.dict_id
            self.insert({
                self.fields[0]: self.dict_id,
                self.fields[1]: el
            })
        return self.dict_index[el]

    def addset(self, aoel):
        return [self.add(el) for el in aoel]


class Reader:
    def __init__(self, file, limit=-1):
        self.file = file
        self.columns = []
        self.counter = 0
        self.skip = 1000000
        self.limit = limit

    def __next__(self):
        if self.limit < 0 or self.counter < self.limit:
            line = self.getline()
            if line:
                self.counter += 1
                values = self.split(line)
                item = {}
                for i in range(len(self.columns)):
                    item[self.columns[i]] = values[i]
                self.informer()
                return item
        self.src.close()
        raise StopIteration


    def __iter__(self):
        self.src = open(self.file, 'r', encoding='utf-8')
        header = self.getline()
        self.columns = self.split(header)
        return self

    def getline(self):
        line = self.src.readline()
        return line

    def informer(self):
        if self.counter % self.skip == 0:
            print(f'Read {self.counter} lines from file {self.file}')


    @staticmethod
    def split(row):
        return row.strip().split("\t")

