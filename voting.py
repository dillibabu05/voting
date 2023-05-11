
nominee1=input("enter the name of the 1st nominee:")
nominee2=input("enter the name of the 2nd nominee:")

#    initially vote count for both must be 0
nm1_votes=0
nm2_votes=0

voter_id=[1,2,3,4,5,6,7,8,9,10]

no_of_voter=len(voter_id)

while True:
    if voter_id ==[]:
        print("Voting session is over !!!")
        if nm1_votes > nm2_votes:
            percentage=(nm1_votes/no_of_voter)*100   # to check the percentage
            print(nominee1,"has won the election with",percentage,"% of votes")
            break
        elif nm2_votes > nm1_votes:
            percentage=(nm2_votes/no_of_voter)*100   # to check the percentage
            print(nominee2,"has won the election with",percentage,"% of votes")
            break
        else:
            print("Both have equal number of votes !!!! Government will decided who will rule")
            break
        
    voter=int(input("enter your voter id:"))
    if voter in voter_id:
        print("you are voter")
        voter_id.remove(voter)  # we will remove so they can't vote again
        print(".................................")
        print(f"to give vote to",{nominee1},"press 1")
        print(f"to give vote to",{nominee2},"press 2")
        print(".................................")
        
        vote=int(input("enter your valuable vote:"))
        if vote ==1:
            nm1_votes +=1
            print(nominee1,"thanks you to give your important vote to them !!")
        elif vote ==2:
            nm1_votes +=1
            print(nominee2,"thanks you to give your important vote to them !!")
        elif vote > 2:
            print("check your pressed key !!")
        else:
            print("you are not a VOTER or you have already voted")