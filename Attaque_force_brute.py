
#algorithme force brute recursive (version1)

liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#def bruteforce(word,length):
 #   if length<=5:
  #      for letter in liste:
   #         if mdp ==word+letter:
    #            print("Vous avez trouvé le mot de passe : "+word+letter)
     #       else:
      #          print(word+letter)
       #         bruteforce(word+letter,length+1)
#mdp = input("Entrez votre mot de passe : ")
#bruteforce('',1)

#algorithme brute force (version2)

mot = input("Entrez votre mot de passe : ")
chaine = str()

def test(chaine, mot):
    if chaine == mot:
        print('le mot de passe est :' + chaine )

def brute_force():
    for l1 in liste:
        chaine = l1
        test(chaine, mot)

    for l2 in liste:
        chaine = l1 + l2
        test(chaine, mot)

    for l3 in liste:
        chaine = l1 + l2 + l3
        test(chaine, mot)

    for l4 in liste:
        chaine = l1 + l2 + l3 + l4
        test(chaine, mot)
        
    for l5 in liste: 
         chaine = l1 + l2 + l3 + l4 + l5 
         test(chaine, mot)
         
brute_force()
