from optparse import OptionParser
import json

class Chess:
    def __init__(self, properties_json=""):
        """
        To validate json file and create an object.
        :param properties_json: name of the json file.
        """
        self.properties_json = properties_json
        self.column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.next_pos = []
        self.direction_met = {'m': self.get_m, 'n': self.get_n, 'o': self.get_o, 'p': self.get_p, 'q': self.get_q,
                              'r': self.get_r, 's': self.get_s, 't': self.get_t}

        flag = 0
        try:
            jsonFile = open(self.properties_json,'r')
        except IOError:
            print "ERROR: File %s not found."%self.properties_json
            flag=1
            exit(1)
        else:
            try:
                self.data = json.load(jsonFile)
            except ValueError:
                print "ERROR: Looks like is an empty json file: %s"%self.properties_json
                flag = 1
                exit(1)
            print "Found %s file"%self.properties_json
        finally:
            if flag != 1:
                print "Object has been created successfully"

    def get_m(self, clmn, row="", dest_pos=8):
        """
        To retuen possible position.
        :param clmn: column index. [0-7]
        :param row: row index. [1-8]
        :param dest_pos: if it is passed, that means it is not X
        :return: returns position
        """
        flag = 0
        if int(dest_pos) != 8:
            flag = 1
            dest_pos = int(clmn) + int(dest_pos)# + 1
            if dest_pos > 8:
                return None
        clmn = clmn + 1
        while clmn <= dest_pos and clmn <= 7:
            n_p = self.column[clmn] + row
            self.next_pos.append(n_p)
            clmn = clmn + 1
        if flag == 1:
            return n_p

    def get_n(self, clmn, row="", dest_pos=0):
        flag = 0
        if int(dest_pos) != 0:
            flag = 1
            dest_pos = int(clmn) - int(dest_pos) #+ 1
            if dest_pos < 0:
                return None

        clmn = clmn - 1
        while clmn >= dest_pos:
            n_p = self.column[clmn] + row
            self.next_pos.append(n_p)
            clmn = clmn - 1
        if flag == 1:
            return n_p

    def get_o(self, clmn, row="", dest_pos=8):
        flag = 0
        if dest_pos != 8:
            dest_pos = int(row) + int(dest_pos) #+ 1
            flag = 1
            if dest_pos > 8:
                return None

        row = int(row) + 1
        while row <= dest_pos and row <= 8:
            n_p = self.column[clmn] + str(row)
            self.next_pos.append(n_p)
            row = row + 1
        if flag == 1:
            return n_p

    def get_p(self, clmn, row="", dest_pos=1):
        flag = 0
        if dest_pos != 1:
            dest_pos = int(row) - int(dest_pos)# + 1
            flag = 1
            if dest_pos < 1:
                return None
        row = int(row) - 1
        while int(row) >= int(dest_pos):
            n_p = self.column[clmn] + str(row)
            self.next_pos.append(n_p)
            row = row - 1
        if flag == 1:
            return n_p

    def get_q(self, clmn, row=""):
        clmn = int(clmn) + 1
        row = int(row) + 1
        while clmn < 8 and row <= 8:
            self.next_pos.append(str(self.column[clmn]) + str(row))
            clmn = clmn + 1
            row = row + 1

    def get_r(self, clmn, row=""):
        clmn = int(clmn) - 1
        row = int(row) - 1
        while clmn >= 0 and row > 0:
            self.next_pos.append(str(self.column[clmn]) + str(row))
            clmn = clmn - 1
            row = row - 1

    def get_s(self, clmn, row=""):
        clmn = int(clmn) - 1
        row = int(row) + 1
        while clmn >= 0 and row <= 8:
            self.next_pos.append(str(self.column[clmn]) + str(row))
            clmn = clmn - 1
            row = row + 1

    def get_t(self, clmn, row=""):
        clmn = int(clmn) + 1
        row = int(row) - 1
        while clmn < 8 and row > 0:
            self.next_pos.append(str(self.column[clmn]) + str(row))
            clmn = clmn + 1
            row = row - 1

    def get_possible_positions(self, current_position="", step=""):
        """
        To process each step and return posiotion.
        :param current_position: position. ex: f4
        :param step: 2m
        :return:
        """
        if step[0] == 'X':
            print "Is starting with X"
            try:
                clmn = self.column.index(current_position[0])
            except ValueError:
                print "Something wrong."
                exit(1)
            else:
                print "STEP: ",step
                return self.direction_met[step[1]](clmn, row=current_position[1])
        elif step[0].isdigit():
            try:
                clmn = self.column.index(current_position[0])
            except ValueError:
                print "Something wrong."
                exit(1)
            else:
                if step[1] in ['m', 'p', 'o', 'n']:
                    temp_pos = self.direction_met[step[1]](clmn, row=current_position[1], dest_pos = step[0])
                    return temp_pos
        else:
            print "ERROR: Invalid step"

    def process_board(self, steps="", current_position=""):
        """
        To process the board. to handle both bilateral and unidirectional steps.
        :param steps: list of steps found in json file.
        :param current_position: position. ex: f4
        :return: a list of positions which the given piece can be moved to.
        """
        result = list()
        bil = 0
        for each_step in steps:
            splitted = each_step.split('-')
            try:
                splitted.remove("")
            except ValueError:
                pass

            #Bilateral directions:
            if len(splitted) == 2:
                bil = 1
                print "A step (%s) found in properties file, which is Bilateral"%(each_step)
                temp_pos = self.get_possible_positions(current_position=current_position, step=splitted[0])
                if temp_pos is not None:
                    result.append(self.get_possible_positions(current_position=temp_pos, step=splitted[1]))
                    continue

            #Unidirectional
            elif len(splitted) == 1:
                if splitted[0] == "":
                    print "Step is empty. Exiting..."
                    exit(1)
                else:
                    print "A step (%s) found in properties file, which is not empty and Unidirectional"%(each_step)
                    result.append(self.get_possible_positions(current_position=current_position, step=splitted[0]))
            else:
                print "Invalid step found in properties file. Exiting..."
                exit(1)
        if bil == 1:
            return result
        else:
            return self.next_pos


    def get_advanceable_positions(self, piece="", current_position=""):
        """
        To return advanceable positions.
        :param piece: Name of the piece. ex: rook
        :param current_position: position. f4
        :return: a list of positions which the given piece can be moved to.
        """
        try:
            if isinstance(self.data[piece]['steps'], list) and len(self.data[piece]['steps']) > 0:
                print "Found steps in properties file for piece %s"%(piece)
            else:
                print "Could not find steps in properties file for piece %s"%(piece)
                exit(1)
        except KeyError as e:
            print "Could not find steps in properties file for piece %s" % (e)
            exit(1)
        else:
            adv_pos = self.process_board(steps=self.data[piece]['steps'], current_position=current_position)
            return adv_pos


def main():
    obj = Chess(properties_json = 'piece_properties.json')
    parser = OptionParser(usage="usage: %prog [OPTIONS]")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    parser.add_option("-i", "--piece", type="string", default="", help="Name of the chess piece. Ex: rook")
    parser.add_option("-o", "--position", type="string", default="", help="A json file which contains properties of chess pieces. Ex: d4")

    parser.set_usage("python %prog --piece=rook --position=a1")

    (options, args) = parser.parse_args()
    #Validate piece names and positions
    if options.position[0] not in obj.column or int(options.position[1]) not in range(1,9):
        print "Error: Invalid current position given"
        exit(1)
    print "%s is at position %s "%(options.piece, options.position)
    positions = obj.get_advanceable_positions(piece = options.piece.lower() , current_position = options.position)
    positions = list(set(positions))
    try:
        positions.remove(None)
    except ValueError:
        pass
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Advanceable positions after processing the board is: ",positions

if __name__ == '__main__':
    main()