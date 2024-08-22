from Booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.close_signin_window()
    bot.change_currency(currency="ARS")
    input("Press any key to exit")