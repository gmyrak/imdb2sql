class Writer:
    def __init__(self, file, fields, name):
        self.name = name
        self.fields = fields
        #self.aof = fields.keys()
        self.storage = open(file, 'w', encoding='utf-8')
        self.active = True
        #self.storage.write('\t'.join(self.fields) + '\n')

    def close(self):
        self.storage.close()
        self.active = False

    def insert(self, item):
        if self.active:
            self.storage.write('\t'.join([str(item.get(f, '')) for f in self.fields]) + '\n')
        else:
            raise('Table is closed')


class Reader:
    def __init__(self, file):
        self.file = file
        self.columns = []

    def __next__(self):
        line = self.src.readline()
        if line:
            values = self.split(line)
            item = {}
            for i in range(len(self.columns)):
                value = values[i]
                #item[self.columns[i]] = (values[i] if values[i] != '\\N' else '')
                item[self.columns[i]] = values[i]
            return item
        else:
            self.src.close()
            raise StopIteration

    def __iter__(self):
        self.src = open(self.file, 'r', encoding='utf-8')
        header = self.src.readline()
        self.columns = self.split(header)
        return self

    @staticmethod
    def split(row):
        return row.strip().split("\t")

