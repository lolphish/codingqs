    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        possible_celeb = 0
        for i in range(n):
            # "possible celeb" should have someone know them and they know no one
            if knows(possible_celeb, i):
                possible_celeb = i
        
        for i in range(n):
            # check if they know anyone
            if possible_celeb != i and knows(possible_celeb, i):
                return -1
            
            # check if everyone knows them
            if possible_celeb != i and not knows(i, possible_celeb):
                return -1
        
        return possible_celeb