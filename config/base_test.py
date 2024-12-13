from services.users.api_users import UsersAPI
from services.wishlist.api_wishlist import WishlistAPI
# from services.orders.api_opders import OrdersAPI
# from services.avatars.api_avatars import AvatarsAPI
from services.games.api_games import GamesAPI
from services.categories.api_categories import CategoriesAPI

class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.wishlist_users = WishlistAPI()
        self.api_games = GamesAPI()
        self.api_categories = CategoriesAPI()
        # self.orders_users = OrdersAPI()
        # self.avatars_api = AvatarsAPI()