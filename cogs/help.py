import discord
import datetime
import os
import random
import asyncio
import contextlib
import json
from discord_components import *
from discord.ext import commands

client = discord.Client

update = "`All bug fixed`"

allembed = discord.Embed(title="OxyGen - Utility Commands",
                         description="""
`ping` , `invite` , `mc` , `badges` , `botinfo` , `av` , `banner` , `banner server`  , `icon server` , `say` , `roleinfo` , `users` , `guilds` , `boosts`
""",
                         color=0x2f3136)
allembed.set_footer(text="Made With ❤️ By OxyGen Development")

modembed = discord.Embed(title="OxyGen - Moderation Commands",
                         description="""
`lock` , `unlock` , `hide` , `unhide` , `purge` , `nick` , `purge`
""",
                         color=0x2f3136)
modembed.set_footer(text="Made With ❤️ By OxyGen Development")

adminembed = discord.Embed(title="OxyGen - Admin Commands",
                           description="""
`fuckban` , `ban` , `getlost` , `fuckoff` ,  `kick` , `roleall` , `hideall` , `unhideall` , `channelnuke` , `addrole` , `removerole`
""",
                           color=0x2f3136)
adminembed.set_footer(text="Made With ❤️ By OxyGen Development")

antinukeembed = discord.Embed(title="OxyGen - Security Feature",
                              description="""
\n>>> **Security Status: Enabled  <:OxyGen_correct:1086535117339631666>\nPunishment: Ban <:OxyGen_ban:1086536040866648105>\n\nAll AntiNuke Features Are Mentioned Below!\n```・Anti Ban\n・Anti Kick\n・Anti Unban\n・Anti Bot Add\n・Anti Channel Create\n・Anti Channel Delete\n・Anti Channel\n・Anti Role Create\n・Anti Role Delete\n・Anti Everyone Ping```**
""",
                              color=0x2f3136)
antinukeembed.set_footer(text="Made With ❤️ By OxyGen Development")

logembed = discord.Embed(title="OxyGen - Logging Commands",
                         description="""
`logging-set` , `logging-config` , `logging-delete`
""",
                         color=0x2f3136)
logembed.set_footer(text="Made With ❤️ By OxyGen Development")

svembed = discord.Embed(title="OxyGen - Server Role Commands",
                        description="""
**__Role Setup Commands__**\n`friend-role-set <role>` , `official-role-set <role>` , `cutie-role-set <role>` , `vip-role-set <role>` , `skid-role-set <role>`\n\n**__Use Below Commands After Setup__**\n`friend <user>` , `official <user>` , `cutie <user>` , `vip <user>` , `skid <user>`\n
""",
                        color=0x2f3136)
svembed.set_footer(text="Made With ❤️ By OxyGen Development")

pfpembed = discord.Embed(title="OxyGen - Auto PFP Commands",
                         description="""
`start` , `stop`\n\nNote: These Cmds Can Only Be Used By Server Owners!
""",
                         color=0x2f3136)
pfpembed.set_footer(text="Made With ❤️ By OxyGen Development")

nsfwembed = discord.Embed(title="OxyGen - Auto NSFW Commands",
                          description="""
`nsfw4k` , `boobs` , `pussy` , `lewd` , `lesbian` , `spank` , `cum`
""",
                          color=0x2f3136)
nsfwembed.set_footer(text="Made With ❤️ By OxyGen Development")

vcembed = discord.Embed(title="OxyGen - Auto Voice Commands",
                        description="""
`vchide` , `vcunhide` , `vcmute` , `vcunmute`
""",
                        color=0x2f3136)
vcembed.set_footer(text="Made With ❤️ By OxyGen Development")

autoembed = discord.Embed(title="OxyGen - Auto-Role Commands",
                          description="""
`autorole add [role]` , `autorole remove [role]`\n\n**__Other Cmds__**\n`roleall <role>`
""",
                          color=0x2f3136)
autoembed.set_footer(text="Made With ❤️ By OxyGen Development")

funembed = discord.Embed(title="OxyGen - Fun Commands",
                         description="""
`qr` , `meme` , `truth` , `dare` , `hack [user] , `gay [user]` , `gender [user]`
""",
                         color=0x2f3136)
funembed.set_footer(text="Made With ❤️ By OxyGen Development")

webembed = discord.Embed(title="OxyGen - Webhook Manager Commands",
                         description="""
`createhook [name]` , `delhook [name]`\n\nNote: These Cmds Can Only Be Used By Server Owners!
""",
                         color=0x2f3136)
webembed.set_footer(text="Made With ❤️ By OxyGen Development")

devembed = discord.Embed(title="OxyGen - Developer Commands",
                         description="""
`jsk` , `g-leave` , `give badge` , `remove badge` , `guilds-ids` , `guilds-show`
""",
                         color=0x2f3136)
devembed.set_footer(text="Made With ❤️ By OxyGen Development")


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["h"])
    @commands.bot_has_permissions(embed_links=True)
    async def help(self, ctx):
        await self.selectboxtesting(ctx)

    async def selectboxtesting(self, ctx):
        devemoji = self.bot.get_emoji(1086590558140637254)
        webemoji = self.bot.get_emoji(1086589845893300264)
        funemoji = self.bot.get_emoji(1086589200071139398)
        autoemoji = self.bot.get_emoji(1086575599298023514)
        nsfwemoji = self.bot.get_emoji(1086588301814800414)
        vcemoji = self.bot.get_emoji(1086586383939932170)
        pfpemoji = self.bot.get_emoji(1086585017058209802)
        serverrolesemoji = self.bot.get_emoji(1086578123979624488)
        logemoji = self.bot.get_emoji(1086576799980462190)
        adminemoji = self.bot.get_emoji(1086573820581785640)
        modemoji = self.bot.get_emoji(1086572113353248838)
        antinukeemoji = self.bot.get_emoji(1086541353506320465)
        allemoji = self.bot.get_emoji(1086546644834734080)
        embed = discord.Embed(
            title="**Help Command Overview :**",
            description=
            f"""<a:OxyGen_dot:1086541780457107486> **Global Prefix**: `=`\n<a:OxyGen_dot:1086541780457107486> **Total Cmd(s)**: {len(self.bot.commands)}  **Guild(s)**: {len(self.bot.guilds)}  **User(s)**: {len(self.bot.users)}\n<a:OxyGen_dot:1086541780457107486> [Invite](https://discord.com/oauth2/authorize?client_id=1086352324252930058&permissions=8&scope=bot) | [Support](https://discord.gg/drWXZrBpKH) | [Vote Soon](https://discord.gg/drWXZrBpKH)\n
            <:OxyGen_blue_dot:1086536511316574288>**__Main__**\n\n<:OxyGen_security:1086541353506320465> **Antinuke**\n<:OxyGen_settings:1086546644834734080> **Utility**\n<:OxyGen_moderation:1086572113353248838> **Moderation**\n<:OxyGen_admin:1086573820581785640> **Admin**\n<:OxyGen_autorole:1086575599298023514> **Autorole**\n<:OxyGen_logging:1086576799980462190> **Logging** \n<:OxyGen_serverroles:1086578123979624488> **Server Roles**\n\n
      <:OxyGen_blue_dot:1086536511316574288> **__Extra__**\n\n<:OxyGen_pfp:1086585017058209802> **Auto Pfp**\n<:OxyGen_vc:1086586383939932170> **Voice Commands**\n<:OxyGen_developer:1086590558140637254> **Developer**""",
            color=0x2f3136)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(
            text="Made With ❤️ By OxyGen Development",
            icon_url=
            "https://media.discordapp.net/attachments/1086376339529015376/1086595669885722724/images.jpeg"
        )
        interaction1 = await ctx.send(
            embed=embed,
            components=[[
                Select(
                    placeholder="OxyGen Help PaneL!",
                    options=[
                        SelectOption(
                            label="Security",
                            description=" Show's You Security Features",
                            value="1",
                            emoji=antinukeemoji),
                        SelectOption(label="Utility",
                                     description="Show's You Utility Commands",
                                     value="2",
                                     emoji=allemoji),
                        SelectOption(
                            label="Moderation",
                            description="Show's You Moderation Commands",
                            value="3",
                            emoji=modemoji),
                        SelectOption(label="Admin",
                                     description="Show's You Admin Commands",
                                     value="4",
                                     emoji=adminemoji),
                        SelectOption(label="AutoRole",
                                     description="Show's You AutoRole Command",
                                     value="5",
                                     emoji=autoemoji),
                        SelectOption(label="Logging",
                                     description="Show's You Logging Command",
                                     value="6",
                                     emoji=logemoji),
                        SelectOption(
                            label="Server Roles",
                            description="Show's You Server Roles Command",
                            value="7",
                            emoji=serverrolesemoji),
                        SelectOption(
                            label="Auto PFP",
                            description=" Show's You Auto PFP Command",
                            value="8",
                            emoji=pfpemoji),
                        SelectOption(label="Voice Commands",
                                     description="Show's You Voice Command",
                                     value="9",
                                     emoji=vcemoji),
                           SelectOption(
                            label="Developers",
                            description="Show's You Developers Command",
                            value="13",
                            emoji=devemoji),
                    ],
                    custom_id="selectboxtesting")
            ]])
        while True:
            try:
                interaction2 = await self.bot.wait_for(
                    "select_option",
                    check=lambda inter: inter.custom_id == "selectboxtesting",
                    timeout=
                    999999999999999999999999999999999999999999999999999999999999999999999
                )
                res = interaction2.values[0]
                if res == "1":
                    await interaction2.send(embed=antinukeembed)
                if res == "2":
                    await interaction2.send(embed=allembed)
                if res == "3":
                    await interaction2.send(embed=modembed)
                if res == "4":
                    await interaction2.send(embed=adminembed)
                if res == "5":
                    await interaction2.send(embed=autoembed)
                if res == "6":
                    await interaction2.send(embed=logembed)
                if res == "7":
                    await interaction2.send(embed=svembed)
                if res == "8":
                    await interaction2.send(embed=pfpembed)
                if res == "9":
                    await interaction2.send(embed=vcembed)
                if res == "10":
                    await interaction2.send(embed=nsfwembed)
                if res == "11":
                    await interaction2.send(embed=funembed)
                if res == "12":
                    await interaction2.send(embed=webembed)
                if res == "13":
                    await interaction2.send(embed=devembed)
                else:
                    pass
            except discord.errors.HTTPException:
                error = "Error"
                print(error)


def setup(bot):
    bot.add_cog(help(bot))