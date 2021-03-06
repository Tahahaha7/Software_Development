import random
try:
    from log import FileLog
except Exception as e:
    print('WARNING: Missing Filelog() in log.py')


class ChristmasTree(object):
    """Cheistmas _tree object.

    Attributes:
        giftlist: List object, containing undecorated gifts
            as str.
        _tree: List object, containing gifts that is on the
            tree.
    """
    try:
        logFile = FileLog()
    except:
        pass

    def __init__(self, giftlist = []):
        self.giftlist = giftlist
        self._tree = None
        
        try:
            self.logFile.info('Christmas _tree created.')
        except:
            pass

    def decorate(self):
        """ Load self.tree according to self.giftlist.

        Output:
            None.
        """
        self._tree = list(self.giftlist)
        self._tree = sorted(self._tree, key = lambda st:len(st))

        try:
            self.logFile.info('Christmas _tree decorated.')
        except:
            pass

    def show(self):
        """ Display the Tree in formatted string according
        to self.tree.

        An error will appear if self._tree is None
        (self.decorate() didn't run before).

        Output:
            multiline string.
        """
        if self._tree == None:
            try:
                self.logFile.error('Called Christmas_tree.show() before Christmas_tree.decorate().')
            except:
                pass
            raise Exception('Christmas _tree has not been decorated')


        #Generate number of gifts in each row
        layers = []
        giftcount = len(self._tree)
        current_len = 0
        while giftcount > 0:
            current_len += 1
            layers.append(current_len)
            giftcount -= current_len
        pos = len(layers) - 1
        while giftcount < 0:
            layers[pos] -= 1
            giftcount += 1
            pos -= 1

        try:
            self.logFile.info('Christmas _tree layers generated.')
        except:
            pass

        #Count number of spaces
        charcount = [0 for _ in range(len(layers))]
        maxcount = 0
        pos = 0
        for i in range(len(layers)):
            for _ in range(layers[i]):
                charcount[i] += len(self._tree[pos]) + 1
                pos += 1
            charcount[i] -= 1
            if charcount[i] > maxcount: maxcount = charcount[i]

        pos = 0
        for i in range(len(layers)):
            print(' ' * ((maxcount - charcount[i] + 1) // 2) + self._tree[pos], end = '')
            for _ in range(1, layers[i]):
                pos += 1
                print(' ' + self._tree[pos], end = '')
            print()
            pos += 1

        try:
            self.logFile.info('Successfully printed the Christmas tree.')
        except:
            pass

    def gift(self, children):
        """ Send the gifts to children.
        A warning will appear if attempting to send gift 
        while the tree is empty.

        Input:
            children: List object, containing names of 
        children.
        Output:
            None.
        """
        random.shuffle(self.giftlist)

        giftcount = 0
        for child in children:
            if len(self.giftlist) == 0:
                print('Oops... The tree is empty!')

                try:
                    self.logFile.warning('Gift request denied: Christmas tree is empty.')
                except:
                    pass

                break
            print(child + ' gets ' + self.giftlist.pop() + '!')
            giftcount += 1

        try:
            self.logFile.info('Successfully gifted ' + str(giftcount) + ' present(s) to children.')
        except:
            pass
        self.decorate()
