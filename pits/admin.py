from pits import app
from pits.models import db, Afisioterapeutas, User, Role, UserRoles
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_admin import BaseView, expose
from flask_user import current_user

#classe do flask-admin
admin = Admin(app, name='microblog', template_mode='bootstrap3')


#classe personalizada para fisioterapeutas que ativa autenticação e grupos autorizados a ver
class AdminView(ModelView):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return True

        if current_user.has_role(['admin','gestor']):
            return True
            
        return True
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))



#define view flask-admin para fisioterapeutas
admin.add_view(AdminView(Afisioterapeutas, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))
admin.add_view(AdminView(UserRoles, db.session))


