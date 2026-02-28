class Solution:

    def city_revenue(self, orders):
        revenue_dict = {}
        ## Write your code here and don't forget to return value.
        for order in orders:
            city = order["city"]
            amount = order["amount"]

            if city in revenue_dict:
                revenue_dict[city]+=amount
            else:
                revenue_dict[city]=amount

        max_city = max(revenue_dict, key=revenue_dict.get)
        return revenue_dict, max_city