class BackBenchers:
    classes = "online"
    
    def depression(self,gf,friends):
        self.gf = gf
        self.friends = friends
        print(f"you status is like {self.gf} gf and your only friends left are {self.friends} ")

        


        # print(" is anyone serious about auto Cad ?")
        # answer = input("yes or no\n")
        
        # if "yes" or "Yes" or "YES" in answer:
        #     print ("how much time will it take to complete auto Cad ")

        # elif "no" or "NO" or "No" in answer:
        #     print("Thanks for Trying ..... ")

        # else:
        #     print("what language is it ? ")


Me = BackBenchers() 
Me.depression()