import random

from WWWL5 import WWWL5
from WWWL5.core.managers import edit_or_reply
from WWWL5.helpers import get_user_from_event
from razan.strings.fun import *

from . import *


@WWWL5.ar_cmd(pattern="رفع قلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه قلبي 🖤 "
    )


@WWWL5.ar_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعه زوجك روحوا خلفوا 😂",
    )


@WWWL5.ar_cmd(pattern="رفع ليفه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**❃ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ طـول عـمـره لـيـفـه اثـبـت يـالـيـفـه 🔪😹 "
    )

@WWWL5.ar_cmd(pattern="رفع اهبل(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**❃ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ طـول عـمـره اهـبـل اي الـجـديـد 🙊😹😹 "
    )


@WWWL5.ar_cmd(pattern="رفع حمار(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفـعـة حـمـار 🦓 "
    )


@WWWL5.ar_cmd(pattern="رفع زوجتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**❃ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 676943:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃  تـم رفعها زوجتك روحو خلفو 😹🤤",
    )


@WWWL5.ar_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**❃ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 203485:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه كلب خليه ينبح 😂🐶",
    )


@WWWL5.ar_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@WWWL5.ar_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**❃ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@WWWL5.ar_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@WWWL5.ar_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**❃ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@WWWL5.ar_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@WWWL5.ar_cmd(pattern="نسبة الجمال(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الجمال لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 🌝"
    )


@WWWL5.ar_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه تاج 👑🔥"
    )


@WWWL5.ar_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**❃ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 203445:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@WWWL5.ar_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@WWWL5.ar_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@WWWL5.ar_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5656828413:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 203485:
        return await edit_or_reply(mention, f"**100%**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@WWWL5.ar_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه حيوان 🐏"
    )


@WWWL5.ar_cmd(pattern="رفع قطه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه قطه 🐈"
    )


@WWWL5.ar_cmd(pattern="رفع ثعبان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه ثعبان 🐍💞"
    )


@WWWL5.ar_cmd(pattern="زواج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم الزواج منه 🌚💞"
    )


@WWWL5.ar_cmd(pattern="طلاق(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم طـلاقـك منه 😂😂"
    )


@WWWL5.ar_cmd(pattern="خلع(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم خـلـعـك مـنـه مـن قـبـل محـكـمـة [ܦ࠭ߺࡋߺוࡅࠦࡅࡅࡅߺ](t.me/FLS_44) 😂"
    )
    
    
@WWWL5.ar_cmd(pattern="الفارات$")
async def _(event):
    zzevent = await edit_or_reply(event, "❃ عزيزي \n❃ انضم الي القناة وستجد جميع الفارات \n❃ [اضغط هنا للانضمام](t.me/FLS_46)   ➪➪➪")