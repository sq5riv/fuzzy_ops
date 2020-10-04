from functools import reduce

class fuzzy_set(object):
    '''Object contains fields and methods of fuzzy set. '''

    def __init__(self, domain  = 0, alpha = 0, function = 0,  alpha_dict = {} ):
        '''domain is list of x points, alpha is list of alpha levels,
        function is list of values of function, alpha_dict is dict of alphacuts'''

        #Fields give by user
        self._domain = domain
        self._alpha = alpha
        self._function = function
        #Fields calculated by methods
        self.OK = False
        self._alpha_cuts = {}
        self.is_convex = True

        if len(alpha_dict) != 0:
            self._alpha_cuts = alpha_dict
        else:
            #Data check 
            self._d_check()
            #Make alpha_cuts
            self.alpha_cuts()
        

    def _convex_check(self, data, alpha_level):

        state = 0
        last_val = '0'
        for i in range(len(data)):
            if data[i] == last_val:
                last_val = data[i]
            else:
                last_val = data[i]
                state +=1

        if state >2:
            print('fuzzy set is not convex at alpha: {}'.format(alpha_level))
            self.convex = False
        
    def _cuter(self, alpha_level):
        '''cuts function for alphacuts'''
        
        tobin = ''
        for point in self._function:
            if point>=alpha_level: tobin +='1'
            else: tobin += '0'

        self._convex_check(tobin, alpha_level)
        
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

    def _domain_check(self, fob):

        if self._domain !=fob.return_domain: raise ValueError("Domains of two fuzzy sets are not equal")
                                                        
    def _d_check(self):
        self._c1(self._domain, 'Dziedzina')
        self._c2(self._domain, 'Dziedzina')
        self._c1(self._alpha, 'Alpha')
        self._c2(self._alpha, 'Alpha')
        self._c3(self._alpha, 'Alpha')
        self._c1(self._function, 'Function')
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

    def return_alphacuts(self):

        return self._alpha_cuts
    
    def return_domain(self):

        return self._domain
    
    def sum(self, summer, alphas = None, Tnorm):
        '''returns new fuzzy set. Summer is second fuzzy set with the same domain, alphas is
        list of alphacuts if None alphas will be copied from this object,
        Tnorm is function to take.'''
        
        ret_alpha_dict = {}
        self._domain_check(summer)
        ac2_list = summer.return_alpha_cuts()
        if alphas is None:
            alphas = self._alpha
        else:
            self._c1(alphas, "Sum Alpha list")
            self._c2(alphas, "Sum Alpha list")
            self._c3(alphas, "Sum Alpha list")

        alphas.sort(reverse = True)
        tmp_alpha = 2.0
        for alpha in alphas:
            middle_val = []
            for  a1, ac1 in  (key, val for key, val in self._alpha_cuts.items() if float(key)>alpha and float(key)<=tmp_alpha):
                for a2, ac2 in (key, val for key,val in ac2_list.items() if float(key)>alpha and float(key)<=tmp_alpha):
                    middle_val.append(Tnorm(a1, ac1,a2,ac2))
            middle_val = reduce( lambda a,b : a&b , middle_val)
            try:
                ret_alpha_dict[alpha] = middle_val & ret_alpha_dict[tmp_alpha]
            except KeyError:
                pass
            tmp_alpha = alpha

        ret_obj = fuzzy_set(domain = self._domain, alpha = alphas, alpha_dict = ret_alpha_dict)

        return ret_obj

def Tnorm_min(a1,ac1,a2,ac2):

    return ac1&ac2
    


if __name__ == '__main__':
    b = list(range(10))
    c = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    d = [0.1,0.2,.3,.4,.5,.6,.7,.8,.6,1]
    a = fuzzy_set(domain = b, alpha = c, function = d)
    e = fuzzy_set(domain = b, alpha = c, function = d)
    a.sum(e,Tnorm = 
    
