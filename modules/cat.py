# Кошка
'''
.cat:: Анимация. \n\n<b>Использование</b>: <code>.cat</code>
'''

from telethon import events
import asyncio
#модуль предложил: t.me/b4yan

def a(client):
	@client.on(events.NewMessage(pattern=r"\.cat", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		await event.edit('''
хуй''')
		await asyncio.sleep(0.5)
		await event.edit('''
пизда''')
		await asyncio.sleep(0.5)
		await event.edit('''
пошел на хуй''')
		await asyncio.sleep(0.5)
		await event.edit('''
уебище''')
		await asyncio.sleep(0.5)
		await event.edit('''
прикол''')
		await asyncio.sleep(0.5)
		await event.edit('''
очкоглаз''')
		await asyncio.sleep(0.5)
		await event.edit('''
все идите на хуй''')
		await asyncio.sleep(0.5)
		await event.edit('''
вот это прикол''')
		await asyncio.sleep(0.5)
		await event.edit('''
я могу вот так вот''')
		await asyncio.sleep(0.5)
		await event.edit('''
и вот так''')
		await asyncio.sleep(0.5)
		await event.edit('''
очень быстро''')
		await asyncio.sleep(0.5)
		await event.edit('''
зачем мне все это я не понимаю''')
		await asyncio.sleep(0.5)
		await event.edit('''
в чем сила брат?''')
		await asyncio.sleep(0.5)
		await event.edit('''
да да да, вот такая вот пизда!''')
		await asyncio.sleep(0.5)
		await event.edit('''
зачем столько разных имен я не понимаю''')
		await asyncio.sleep(0.5)
		
 


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass
