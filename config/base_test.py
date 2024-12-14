from services.users.api_users import UsersAPI
from services.wishlist.api_wishlist import WishlistAPI
from services.orders.api_opders import OrdersApi
# from services.avatars.api_avatars import AvatarsAPI
from services.games.api_games import GamesAPI
from services.categories.api_categories import CategoriesAPI
from services.cart.api_cart import CartAPI

class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.wishlist_users = WishlistAPI()
        self.api_games = GamesAPI()
        self.api_categories = CategoriesAPI()
        self.api_opders = OrdersApi()
        # self.avatars_api = AvatarsAPI()
        self.api_cart = CartAPI()
