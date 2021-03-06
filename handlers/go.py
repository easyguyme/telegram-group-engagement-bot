from app import *
from main.functions import Action

keyboard = types.InlineKeyboardMarkup(row_width=2)
# a = types.InlineKeyboardButton(text=emoji.emojize(":memo: Check :memo:", use_aliases=True), callback_data="check")
a = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Dx15 List", use_aliases=True), callback_data="list")
keyboard.add(a)


@bot.message_handler()
def echo(msg):
    """
    Checking The User's Message Within The Licensed Group
    """

    message_format = "Dx15 @instatravel.lifestyle https://www.instagram.com/p/CCk4PN9sz4S/"

    if msg.chat.type == "group" or msg.chat.type == "supergroup":

        #Check the message format
        text = msg.text

        message = text.split(" ")

        username = message[1].strip("@")

        if len(message) != 3:
            reply = bot.reply_to(
                msg,
                f"""
Wrong Format! The right format is
{message_format}
                """,
                disable_web_page_preview=True
            )            

        elif len(message[2].strip("/").split("/")) == 5:

            link = message[2]

            action = Action(username, link)
            
            action.get_user_id()
            post = action.get_media_id()

            if post is None:
                reply = bot.reply_to(
                    msg,
                    f"This post was not found in {username}'s timeline feed"
                )
            else:
            
                ####CHECK IF USER HAS PERFORMED LIKE ACTIONS
                action.check_likes()
                action.check_comments()

                status = action.get_status()

                if status != True:
                    reply = bot.reply_to(
                        msg,
                        emoji.emojize(f":x: {status}", use_aliases=True)
                    )
                else:
                    bot.reply_to(
                        msg,
                        emoji.emojize(f"@{msg.from_user.first_name} :heavy_check_mark: Approved", use_aliases=True)
                    )
                    action.add_to_list()

        else:
            reply = bot.reply_to(
                msg,
                f"""
Wrong Format! The right format is
{message_format}
                """,
                disable_web_page_preview=True
            )


    elif msg.chat.type == "private":

        message = """
<b>:bangbang: STOP Liking & Commenting :bangbang:</b>

:raising_hand: Join the Premium Subscribers and post without engaging back or get auto comments every time you post to our pods :raising_hand:

:point_right: Contact admin:
 @codefred :phone:
"""
        
        reply = bot.reply_to(
            msg,
            emoji.emojize(message, use_aliases=True),
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=keyboard
        )

    else:    
        pass


    try:
        bot.delete_message(msg.chat.id, msg.message_id)
        time.sleep(60)

        bot.delete_message(msg.chat.id, reply.message_id)
    except:
        pass
    



