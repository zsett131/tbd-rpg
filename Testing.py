from PlayerBase import PlayerBase


class Testing:
    
    A = PlayerBase()
    A.setplayercurrenthealth(10)
    print(A.getplayerExpCap())
    A.addplayerExp(100)
    print(A.getplayerLevel())
    print(A.getplayerExpCap())
    A.addplayerExp(200)
    print(A.getplayerExpCap())
    print(A.getplayerExp())
    A.addplayerExp(300)
    print(A.getplayerExpCap())

