from tqdm import trange


class node:
    def __init__( self, id, index, deep, fatherExist, father, objList = [] ):
        self.id          = id
        self.index       = index
        self.deep        = deep
        self.fatherExist = fatherExist
        self.objList     = objList

        if( self.fatherExist == True ):
            self.father = father

    class chields:
        def __init__( self, nth = 0, list = [], auxList = [] ) :
            self.nth       = nth
            self.__list    = list
            self.__auxList = auxList

        @property
        def list( self ):            
            if( len( self.__auxList ) == 1 ):
                self.__list.insert( self.__auxList[0][0], self.__auxList[0][1] )
                self.__auxList.pop()

                return self.__list
            else: # len( __auxlist ) = 0 
                return self.__list
        
        @list.setter
        def list( self, append ):
            self.__list.append( append )

        @property
        def stack( self ):
            return self.__auxList

    class brothers:
        def __init__( self, fatherExist, chieldsListIndex ,father, id ):
            self.fatherExist = fatherExist

            if( fatherExist == True ):
                self.__chieldsListIndex = chieldsListIndex
                self.father             = father

        @property
        def nth( self ):
            if( self.fatherExist == True ):
                return self.father.chields.nth - 1
            else:
                return 0
        @property
        def list( self ):
            if( self.fatherExist == True ):
                mySelf = self.father.chields.list[ self.__chieldsListIndex ] 
                list = self.father.chields.list
                list.pop( self.__chieldsListIndex )

                self.father.chields.stack.append( [ self.__chieldsListIndex, mySelf ] )
                # print( self.father.chields.auxList[0][1].id )

                return list
            else:
                return []

    def addSon( self, idSon ):
        index            = len( self.objList )
        deep             = self.deep + 1
        fatherExist      = True
        father           = self
        objList          = self.objList
        chieldsListIndex = len( self.chields.list )

        el = node( idSon, index, deep, fatherExist, father, objList )
        el.chields = node.chields( 0, [], [] )
        el.brothers = node.brothers( fatherExist ,chieldsListIndex ,father, idSon )

        self.chields.nth  = self.chields.nth + 1
        self.chields.list = el

        self.objList.append( el )

        return el

def creatNode( id, index, deep,
 fatherExist, father, chieldsListIndex, 
 objList = [] ):
    el          = node( id, index, deep, fatherExist, father, objList )
    el.chields  = node.chields( 0, [], [] )
    el.brothers = node.brothers( fatherExist, chieldsListIndex, father, id )

    return el

majorList = [] 

majorList.append( 
    creatNode( "Name the first node here", 0, 0, # Name the first node 
     False, None, None,
     majorList ) 
)

# User space below 

majorList[0].addSon( "Node_001" )
majorList[0].addSon( "Node_002" )
majorList[0].addSon( "Node_003" )
majorList[0].addSon( "Node_004" )
majorList[0].addSon( "Node_005" )

majorList[1].addSon( "Node_011" )
majorList[1].addSon( "Node_012" )
majorList[1].addSon( "Node_013" )
majorList[1].addSon( "Node_014" )
majorList[1].addSon( "Node_015" )

majorList[3].addSon( "Node_033" )
majorList[3].addSon( "Node_034" )
majorList[3].addSon( "Node_035" )

majorList[9].addSon( "Node_093" )
majorList[9].addSon( "Node_094" )
majorList[9].addSon( "Node_095" )

for k in range( len( majorList ) ):
    if( majorList[k].fatherExist == True ):
        print( "\nfilhos de :", majorList[k].id,
        "( pai: ", majorList[k].father.id, " )" )
    else:
        print( "\nfilhos de :", majorList[k].id,
        "( Raiz )" )
    for i in range( majorList[k].chields.nth ):
        print( majorList[k].chields.list[i].id )
    print( "\n" )

    for i in range( majorList[k].chields.nth ):
        print( "    Irmãos de: ", majorList[k].chields.list[i].id )
        for j in range( len( majorList[k].chields.list[i].brothers.list ) ):
            print( "    ", majorList[k].chields.list[i].brothers.list[j].id )
        print( "\n" )

