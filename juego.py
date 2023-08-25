# from pygments import highlight
# primero tiene que tener instalado python para que corra ursina con tu juego  : luego solo lo puedes verificar viendo todos tus modulos con pip list 
from ursina import *  # importamos todos los archivos de ursina y que nos importe todo con el * arterisco 
from ursina.prefabs.first_person_controller import FirstPersonController # utilizaremos uno de los tantos paquetes que tiene ursina : xd si llegas a este punto de repositorio no soy de crear miucho esto pero sigue asi : 👍
# le decimos que nos incorpore cosas q ya estan definidas por el mismo ursina : el contralador : first_person_controller es lo que nos interesa y eso lo importaremos FirstPersonController  
app = Ursina()   # crear una  app llamamos a ursina con : Ursina()
class Voxel(Button):  # la clase principal sera el boxel y va a heredar de el tipo boton : Button que esta entre parentesis tiene varias modulos por asi decirlas : la cosa que ya lo tiene definidos para el funcionamiento de nuestro juego
    def __init__(self,position=(0,0,0)): # el def __init__ siempre se pone al crearte una clase estas def : son funciones : bueno asi las llamo yo el self es obligatorio ya que es una forma de referirse asi mismo 
        # y el otro parametro q seria el position que ya le estamos indicando sus posiciones definidas (x,y,z)
        super().__init__(  # el metodo super().__init__ va a ser el inicializador padre : boton : que es la herencia q indicamos en el Voxel : el super init es una forma de buscar la clase tal e ir a la clase padres y otras hasta encontrar el boton q estamos intentando encontrar esto es Mas Sobre POO en mis repositorios ay unos ejercicios
            parent = scene,  # q el objeto pertenece a la jerarquia de scene : que si no saben q es jerarquia es una forma de buscar ejemplo (a,b) va a la clase a(y tiene una herencia que es c : se veria asi a(c)) va en c y c tiene una jerarquia con d y se veria c(d)  y si en d tampoco no encuentra lo que queria buscar o lo que quiere encontra se va al otro parametro del inicio y asi con todo lo demas
            position = position, #y tambien le pasamos la posicion que tendra que lo especificamos en el def__init__(que su posicion es x , y , z (0,0,0))
            model = 'cube',  # el tipo de modelo q vamos a usar para el objeto : lo indicamos q sea cube y le tenemos q pasar un origen 
            origin_y = 0.5,  # es una de las posiciones q viene en ursina :c 
            texture = 'grass',  # el valor de textura ponemos grass pa q se vea todo como verde parecidaso a minimicraft 
            color = color.rgb(225,155,200),  #  podes cambiar el color 
            highlight_color = color.lime,  # 
        )

    def input(self, key):  # aca indicamos si machucamos tal tecla q vamos a ser : en este caso solo agregar bloquey y destroy 
        if self.hovered:  
            if key == "left mouse down":  # comprobar si esta presionando el mouse down : hacia abajo => 
                voxel = Voxel(position= self.position + mouse.normal)# crear un voxel que sea de  esta clase que lo definimos Voxel(la misma posicion que te encuentras , y ademas calcular la posicion normal del mouse )
                
            if key == "right mouse down":  # si as presionado una tecla y si la tecla es right mouse down 
                destroy(self)  # destroy el objeto q esta seleccionado a donde apunta el mouse 
# esas propiedades ya viene definidas en los botones Y como heredamos de Boton se nos da mas  facil 
chunkSize = 30  # creamos un  chunkSize que tamaño tiene que es 16 

for z in range(chunkSize):  # y hacemos un bucle for  : que z va a rrecorrer hasta el rango de chunkSize igual que con x que me cree un boxel 
    for x in range(chunkSize):
        voxel = Voxel(position=(x,0,z))  # aca le indicamos q nos cree un terreno como el modo creativo en el eje  x y z : x => en profundidad  : z => tambien lo que sera el ancho  y el alto lo dejamos en 0 : y => 0

player = FirstPersonController()  # para el lado de persona si no no haria nada el personaje : como ya teniamos importado el FirstPersonController   :=> y que nos cree un objeto de un tipo para que sea nuestro jugador poder moverno y todo 


app.run()  # para inicializar al juago : ya que el programa se llama app le decimos app.run() arranca el juegoo goo.




