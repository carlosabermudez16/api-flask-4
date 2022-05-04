APIrest que permite que cualquiera pueda consumirla
ya que se subirá a la web.
Nosotros utilizaremos Heroku, el cual es una plataforma
de servicios en la nube conocido como PaaS(plataforma como un servicio)
en donde se pueden alojar proyectos en su hosting.

A Heroku solo le dices qué lenguaje de backend estás utilizando o qué base 
de datos vas a utilizar y te preocupas únicamente por el desarrollo de tu 
aplicación. Heroku ejecuta sus aplicaciones a traves de contenedores

Requerimientos para usar los servicios de Heroku:
1.  archivo Procfile en la raiz del proyecto
2.  archivo requirements.txt
3.  tener el proyecto subido a github, primero nos vamos a github y creamos un
    proyecto.
4.  archivo .gitignore con la información que queremos que se ignore

comandos de git:
--> git init
--> git add -A
--> git commit -m "cualquier comentario"
--> este lo copias del proyecto creado en github:   
    git remote add origin https://github.com/carlosabermudez16/...
--> git push
    toma el comando que te sale a hacer click:
    git push --set-upstream origin master

por último actualizas en la web del proyecto creado en github

5. En Heroku hacemos click en new-->created new app : se rellenan los campos y click en create app
6. Enlazamos el repositorio de github haciendo click en connect to GitHub,
   una vez conectado buscamos el repositorio y lo cenectamos, después hacemos click
   en deploy branch y click en view.

