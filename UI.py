class UI:
    @staticmethod
    def homepage():
        print('--------MFVS--------')
        print('Login with:')
        print('1. Customer Account')
        print('2. Owner Account')
        print('3. Create Customer Account')
        print('9. Exit')

    @staticmethod
    def customer_homepage():
        print('--------MFVS--------')
        print('1. View Product')
        print('2. Search Product')
        print('3. Sort Product')
        print('4. Modify Account')
        print('5. Delete Account')
        print('9. Exit')

    @staticmethod
    def view_product(products):
        print('--------View Product--------')
        for i in range(len(products)):
            print('{}. {}'.format(i + 1, products[i].name))
        print('7. Previous Page')
        print('8. Next Page')
        print('9. Back to Home Page')

    @staticmethod
    def view_product_detail(product):
        print('--------View Product Detail--------')
        print(product)
        print('1. Add to Cart')
        print('2. Back to Previous Page')
        print('9. Exit')

    @staticmethod
    def sort_product():
        print('--------Sort Product--------')
        print('1. Sort by Name(Ascending Order)')
        print('2. Sort by Name(Descending Order')
        print('3. Sort by Price(Low to High')
        print('4. Sort by Price(High to Low')