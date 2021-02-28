class User:

    def __init__(self, username: str, password: str, email: str, location: str) -> None:
        """signup when a new user gets created
        :params location: home location connected with the user -> ranking based on location (coming soon)
        """
        self.__signup(username, password, email, location)

    def __signup(self, username: str, password: str, email: str, location: str) -> None:
        """create a user account
        :params: set provided parameters as user account data
        """
        self.username = username
        self.__password = password
        self.__email = email
        self.location = location
        self.__credit_score = 0

    def login(self, username: str, password: str) -> str:
        """login if username and password match up"""
        if username == self.username:
            if password == self.__password:
                print("Logged in.")
                self.logged_in = True
            else:
                print("Wrong Password.")

    def logout(self) -> None:
        self.logged_in = False

    def get_credit_score(self) -> str:
        """display the user's current credit balance"""
        print(f"Your current credit balance: {self.__credit_score}")

    def add_credits(self, credits: int) -> None:
        """recalculate credit balance
        :params credits: obtained credits from means of travel
        """
        self.__credit_score += credits

    def get_reward(self, reward: str) -> None:
        """add provided reward type to your trophy case
        :params reward: obtained reward type
        """
        if reward == "bonsai":
            self.reward_bonsai = 1
        elif reward == "tree":
            self.reward_tree = 1
        elif reward == "flower":
            self.reward_flower = 1

    def get_trophy_case(self) -> tuple:
        """get all (un)obtained rewards
        :return: tuple of reward types, 0 = not obtained, 1 = obtained
        """
        return self.reward_bonsai, self.reward_tree, self.reward_flower

    def get_location(self) -> str:
        print(f"Your home location is {self.location}")
