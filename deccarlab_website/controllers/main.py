
from datetime import datetime
from werkzeug.exceptions import Forbidden, NotFound


from odoo import fields, http, SUPERUSER_ID, tools, _

from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale





class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True,)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(WebsiteSaleInherit,self).shop(page, category, search, min_price, max_price, ppg, **post)
        categ = res.qcontext.get('category')
        res.qcontext.update({'categories' : categ})
        return res