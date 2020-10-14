from functools import reduce

class fuzzy_set(object):
    '''Object contains fields and methods of fuzzy set.'''

    def  __init__(self, domain = None,  function = None, alphas = None, alpha_dict = {}):
        '''Domain is list of x, function is given function between 0-1, alphas is list of alphas level,
        alpha_dict is dict of alpha cuts'''

        #Fields give by user
        self._domain = domain
        self._alpha = alphas
        self._function = function
        self._alpha_dict = alpha_dict
        #Fields calculated by methods
        self.OK = False #is object ok
        self.is_convex = None
        self.made_by_func = None
        #check for data correct
        self._check1()
        self._alphator()

    def _alphator(self):
        '''makes alphacuts from function'''

        for alpha in self._alphas:
            tmp_list = []
            isup = False
            for i in enumerate(len(self(domain))):
                if self._function[i]>=alpha and isup == False:
                    tmp_list.append(self._domain[i])
                    isup = True
                elif self._function[i]<alpha and isup == True:
                    tmp_list.append(self._domain[i-1])
                    isup = False
            if len(tmp)%2 == 1:
                tmp_list.append(self._domain[-1])
            self._alpha_dict[alpha] = tmp_list

        self.is_convex()
            
            
                           
    def _c1(self, data, name):
        '''checks is None or list or tuple'''

        if data != None:
            if not isinstance(data, (list,tuple)):
                raise TypeError('%s have to be list or tuple'%name)

    def _c2(self, data, name):

        if data!= None:
            if not all([isinstance(a, (int,float)) for a in data]):
                self.OK = False
                raise TypeError('%s values have to be int or float'%name)

    def _c3(self, data, name):

        if data!=None:
            if not all([a<=1 and a>=0 for a in data]):
                self.OK = False
                raise ValueError('%s values have to be between 0 and 1'%name)

    def _c4(self):

        if self._domain!= None and self._function !=None:
            if not len(self._domain) == len(self._function):
                raise ValueError('Length of data and domain have to be the sam length')            

    def _c5(self):

        if self._domain == None and self._alpha == None and self._function == None:
            self.made_by_func = False
        else:
            self.made_by_func = True

    def _c6(self):
        '''check for alphacuts dictionary is correst'''

        if not  isinstance(self._alpha_dict, dict):
            raise: TypeError('alpha_dict have to by dict')
        if self.made_by_func == False:
            for k,v in self._alpha_dict.items():
                if k<1 and k>0: raise ValueError('Alpha levels have to be between 0 and 1')

                if not isinstance(v, tuple): raise TypeError('Alphacuts have to be tuple')

    def is_convex(self):
        '''check for fuzzy set is convex'''

        for k,v in self._alpha_dict.items():
            if len(v)<2:
                self.is_convex = False
            else:
                self.is_convex = True
                
    def _check1(self):
        '''checks given data'''

        #domain checks input data.
        self._c1(self._domain, 'domain')
        self._c1(self._function,'function')
        self._c2(self._domain, 'domain')
        self._c2(self._function, 'function')
        self._c3(self._function, 'function')
        self._c3(self._alpha, 'alpha')
        self._c4()
        self._c5()
        self._c6()
        if self.made_by_func == False:
            self.is_convex()

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    b =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    c= [0.1,0.3,0.5,0.9]
    z = fuzzy_set(a,b,c)
