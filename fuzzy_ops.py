

class fuzzy_set(object):
    '''Object contains fields and methods of fuzzy set. '''

    def __init__(self, domain, alpha, function):

        #Fields give by user
        self._domain = domain
        self._alpha = alpha
        self._function = function
        #Fields calculated by methods
        self.OK = False
        self._alpha_cuts = {}

        #Data check 
        self._d_check()
        #Make alpha_cuts
        self.alpha_cuts()
        
    def _cuter(self, alpha_level):
        
        tobin = ''
        for point in self._function:
            if point>=alpha_level: tobin +='1'
            else: tobin += '0'

        retval = int(tobin, 2)
        return retval
            
    def _c1(self, data, name):
        
        if not isinstance(data, (list, tuple)):
            self.OK = False
            raise TypeError('%s have to be list or tuple'%name)

    def _c2(self, data, name):

        if not all([isinstance(a, (int,float)) for a in data]):
            self.OK = False
            raise TypeError('%s values have to be int or float'%name)

    def _c3(self, data, name):

        if not all([a<=1 and a>=0 for a in data]):
            self.OK = False
            raise ValueError('%s values have to be between 0 and 1'%name)

    def _c4(self):

        if not len(self._domain) == len(self._function):
            raise ValueError('Length of data and domain have to be the sam length')
        
    def _d_check(self):
        self._c1(self._domain, 'Dziedzina')
        self._c2(self._domain, 'Dziedzina')
        self._c1(self._alpha, 'Alpha')
        self._c2(self._alpha, 'Alpha')
        self._c3(self._alpha, 'Alpha')
        self._c1(self._function, 'Fnction')
        self._c2(self._function, 'Function')
        self._c4()
        self.OK = True

    def alpha_cuts(self):
        '''updates aplha cuts'''

        for a in self._alpha:
            if not a in self._alpha_cuts:
                self._alpha_cuts[a] = self._cuter(a)

    def alpha_downdate(self, alpha):
        '''downdate some alpha from alphalist'''

        if alpha in self._alpha_cuts: del self._alpha_cuts[alpha]
        else: raise ValueError('There is not %s in alpha list' %alpha)

    def alpha_show(self):
        '''shoe list of alphacuts'''

        return list(self._alpha_cuts.keys())
        
    def alpha_update(self, alpha):
        '''updates list of levels of aplhacuts'''

        self._c1(alpha, 'New alpha')
        self._c2(alpha, 'New alpha')
        self._c3(alpha, 'New alpha')
        self._alpha.extend(alpha)
        self.alpha_cuts()
        self.OK = True

    
            

if __name__ == '__main__':
    b = list(range(10))
    c = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    d = [0.1,0.2,.3,.4,.5,.6,.7,.8,.9,1]
    a = fuzzy_set(b,c,d)
    print(a.__dict__)
    c = [0.33,0.66]
    a.alpha_update(c)
    print(a.__dict__)
    a.alpha_downdate(0.1)
    print(a.__dict__)
    print(a.alpha_show())
    
