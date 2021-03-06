#!/usr/bin/env python
import sys
from minecraft import authentication
from minecraft.exceptions import YggdrasilError
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound
import json
from rich import print
from dotenv import load_dotenv
import os
from ChatMessage import ChatMessage

print_log_on_exit = True
log = [ChatMessage.LogMsg("Started app.py", color="#008888")]


def main():
    load_dotenv("crd.env")
    USR = os.getenv('USR')
    PSS = os.getenv('PSS')
    auth_token = authentication.AuthenticationToken()
    try:
        auth_token.authenticate(USR, PSS)
    except YggdrasilError as e:
        print(e)
        sys.exit()
    print(f"Logged in as {auth_token.username}...")
    connection = Connection("play.hypixel.net", 25565, auth_token=auth_token)

    def handle_join_game(join_packet):
        print('[bold green][!] Connected...[/]')

    connection.register_packet_listener(handle_join_game, clientbound.play.JoinGamePacket)

    def print_chat(chat_packet):
        json_data = json.loads(chat_packet.json_data)
        # Todo fixing friend list detection

        try:
            if json_data['text'].startswith("From ") or json_data['text'].startswith("To ") and json_data['color'] \
                    == "light_purple":
                print(ChatMessage.Hypixel.Global.PrivateMessage(json_dict=json_data).formatted())
                return
        except (IndexError, KeyError) as e:
            log.append(ChatMessage.LogMsg(e, "Private messages"))

        try:
            if json_data['extra'][0]['text'] == " §b>§c>§a>§r " or "§6joined the lobby!" in json_data['extra'][0][
                'text']:
                print(ChatMessage.Hypixel.Global.LobbyJoinMessage(json_dict=json_data).formatted())
                return
        except (IndexError, KeyError) as e:
            log.append(ChatMessage.LogMsg(e, "Lobby join messages"))
        # TODO First message is being identified as mystery box - maybe it should be "and" instead of "or"?
        try:
            if json_data['extra'][2]['text'] == "Mystery Box" or json_data['extra'][3]['text'] == "Mystery Box" and \
                    json_data['extra'][2]['color'] == "aqua" or json_data['extra'][3]['color'] == "aqua":
                print(ChatMessage.Hypixel.Global.MysteryBoxes(json_dict=json_data).formatted())
                return
        except (IndexError, KeyError) as e:
            log.append(ChatMessage.LogMsg(e, "Got Mystery Box announcement"))

        try:
            if json_data['text'] == "Friend > " and json_data['color'] == "green":
                print(ChatMessage.Hypixel.Global.FriendStatus(json_dict=json_data).formatted())
                return
        except (IndexError, KeyError) as e:
            log.append(ChatMessage.LogMsg(e, "Friend status"))

        try:
            if "✫" in json_data['extra'][0]['text']:
                print(ChatMessage.Hypixel.HypixelBedwarsLobby(json_dict=json_data).formatted())
                return
        except (IndexError, KeyError) as e:
            log.append(ChatMessage.LogMsg(e, "Bedwars lobby player chat"))

        try:
            if json_data['text'] == "You are AFK. Move around to return from AFK." and json_data['color'] == "red":
                print(ChatMessage.Hypixel.Global.LimboMessage(json_dict=json_data).formatted())
                return
        except (IndexError, KeyError) as e:
            log.append(ChatMessage.LogMsg(e, "AFK"))

        try:
            if json_data['extra'][3]['text'].startswith(">>") or json_data['extra'][2]['text'].startswith("<<") \
                    and json_data['extra'][3]['color'] == 'yellow' or json_data['extra'][2]['color'] == 'yellow':
                print(ChatMessage.Hypixel.Global.FriendList(json_dict=json_data).formatted())
                return
        except Exception as e:
            print(e)
            print(json_data)
            # log.append(ChatMessage.LogMsg(e, json_data, raw=True)) - fills up log
            log.append(ChatMessage.LogMsg(e, "Final catch exception - likely unsupported message."))
            pass

    connection.register_packet_listener(print_chat, clientbound.play.ChatMessagePacket)
    connection.connect()

    while True:
        try:
            text = input()
            packet = serverbound.play.ChatPacket()
            packet.message = text
            connection.write_packet(packet)
        except KeyboardInterrupt:
            print("Disconnecting...")
            if print_log_on_exit:
                for log_msg in log:
                    log_msg.printLogMsg()
            sys.exit()


if __name__ == "__main__":
    main()
