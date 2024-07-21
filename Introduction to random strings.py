class gc_content_string:
    def gc_content_string_(gc_content,string):
        list_of_calcs=[]
        for gc in gc_content:
            calc=0
            for i in range(len(string)):
                if string[i]=='A' or string[i]== 'T':
                   calc+= math.log((1-gc)/2,10)
               
                elif string[i]=='C' or string[i]== 'G':
                     calc+=math.log(gc/2,10)
        
            list_of_calcs.append(round(calc,3))
        return print(list_of_calcs)
if __name__ == "__main__":
  import math 
  dna_string='ACGATACAA'
  gc_content=[0.129,0.287,0.423, 0.476, 0.641, 0.742, 0.783]
  gc_content_string.gc_content_string_(gc_content,dna_string)
