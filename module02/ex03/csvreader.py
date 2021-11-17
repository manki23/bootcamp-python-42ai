import csv


class CsvReader():
    def __init__(
            self,
            filename=None,
            sep=',',
            header=False,
            skip_top=0,
            skip_bottom=0
    ):
        self.sep = sep
        self.has_header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.line_length = 0
        self.data = []
        self.filename = filename

    def ft_read_line(self):
        line = self.file_obj.readline()
        line = line.strip().split(self.sep)
        line = [elem.strip() for elem in line]
        if len(line) == 1 and self.line_length > 1:
            return None
        line = [elem.strip('"') for elem in line]
        return line

    def __enter__(self):
        try:
            self.file_obj = open(self.filename, 'r')
            self.close_file = True
        except FileNotFoundError:
            self.close_file = False
            return None
        line = self.ft_read_line()
        line_count = 0
        while line:
            if line_count == 0:
                self.line_length = len(line)
                if self.has_header:
                    self.header_data = line
                else:
                    self.data.append(line)
            elif any(elem == '' for elem in line):
                return None
            elif len(line) == self.line_length:
                self.data.append(line)
            else:
                return None
            line = self.ft_read_line()
            line_count += 1

        return self

    def __exit__(self, type, value, traceback):
        if self.close_file:
            self.file_obj.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
            nested list (list(list, list, ...)) representing the data.
        """
        if self.skip_bottom > 0:
            return self.data[self.skip_top:-self.skip_bottom]
        else:
            return self.data[self.skip_top:]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        if self.has_header is True:
            return self.header_data
        else:
            return None
