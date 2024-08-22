from Booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    print("Bot landed on the first page")