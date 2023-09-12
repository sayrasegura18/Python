from flask import render_template, redirect, flash
from . import clientes
import app
from .form import RegistrarClientesForm, NewClientesForm, EditClientesForm
import os

#rutas del modulo clientes "clientes"
@clientes.route("/listar")
def listar():
    # definir el formulario
    form = RegistrarClientesForm()
    # listar los clientes utilizando 
    # modelos
    clientes = app.models.Cliente.query.all()
    return render_template("index.html",
                           clientes =  clientes)



@clientes.route("/nuevo",
                 methods=["GET", "POST"])
def nuevo():
     # definir el formulario
    form = NewClientesForm()
    #definir el objeto cliente vacio
    c = app.models.Cliente()
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        flash ("Cliente registrado")
        return redirect("/clientes/listar")

    return render_template("registrar_cliente.html",
                           form = form)

@clientes.route("/editar/<cliente_id>",
                 methods = ['GET','POST'])
def editar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientesForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect("/clientes/listar")
    return render_template("registrar_cliente.html",   
                           operacion = "Actualizar",                          
                           form = form)

@clientes.route('/eliminar/<cliente_id>')
def eliminar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Cliente eliminando correctamente")
    return redirect("/clientes/listar")
