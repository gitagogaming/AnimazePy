__copyright__ = """
    This file is part of the AnimazePy project.
    Copyright (C) 2023 Gitago

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
import websocket
import logging

class AnimazeWrapper:
    """
    A Python wrapper for the Animaze API.

    Args:
        dev_name (str): The developer name or identifier. Defaults to "MyDevName".
        websocket_url (str, optional): The URL of the WebSocket server. Defaults to "ws://localhost:9000".

    Attributes:
        dev_name (str): The developer name or identifier.
        websocket_url (str): The URL of the WebSocket server.
        ws (websocket._core.WebSocket): The WebSocket connection object.
        logger (logging.Logger): The logger object for logging messages.
    """
    def __init__(self, dev_name="MyDevName", websocket_url="ws://localhost:9000"):
        self.dev_name = dev_name
        self.websocket_url = websocket_url
        self.ws = None
        self.logger = logging.getLogger(__name__)
    

    def connect(self):
        try:
            self.ws = websocket.create_connection(self.websocket_url)
            self.logger.info("WebSocket connection opened successfully.")
            return self.ws
        except ConnectionRefusedError:
            self.logger.error("Connection was actively refused by the target machine.")
            self.logger.error("Is Animaze running?")
            return "Connection was actively refused by the target machine. Is Animaze running?"
        except Exception as e:
            self.logger.error(f"Failed to open WebSocket due to: {str(e)}")
            return
 


    def disconnect(self):
        if self.ws is not None:
            self.ws.close()
            self.ws = None
            self.logger.info("WebSocket connection closed successfully.")
            return "WebSocket connection closed successfully."
        else:
            self.logger.error("No WebSocket connection to close.")
            return "No WebSocket connection to close."

    def send_command(self, command):
        try:
            if self.ws is None:
                self.logger.error("WebSocket connection is not open. Call 'open_websocket' first.")
                return

            self.ws.send(json.dumps(command))
            response = self.ws.recv()
            return json.loads(response)
        except Exception as e:
            self.logger.error('Failed to send command due to: ' + str(e))


    
    def get_item_icon(self, avatar_name:str):
        command = {
            "action": "GetItemIcon",
            "id": self.dev_name,
            "name": avatar_name
        }
        return self.send_command(command)


    def get_idle_anims(self):
        command = {
            "action": "GetIdleAnims",
            "id": self.dev_name
        }
        return self.send_command(command)


    def get_special_actions(self):
        command = {
            "action": "GetSpecialActions",
            "id": self.dev_name
        }
        return self.send_command(command)

    def get_poses(self):
        command = {
            "action": "GetPoses",
            "id": self.dev_name
        }
        return self.send_command(command)
    

    def get_emotes(self):
        command = {
            "action": "GetEmotes",
            "id": self.dev_name
        }
        return self.send_command(command)

    def get_cameraTransform(self):
        command = {
            "action": "GetCameraTransform",
            "id": self.dev_name
        }
        return self.send_command(command)

    def get_camera_fov(self):
        command = {
            "action": "GetCameraFOV",
            "id": self.dev_name
        }
        return self.send_command(command)


    def set_camera_fov(self, fov:float):
        command = {
            "action": "SetCameraFOV",
            "id": self.dev_name,
            "fov": fov
        }
        return self.send_command(command)

    def broadcast(self, choice:bool):
        command = {
            "action": "Broadcast",
            "id": self.dev_name,
            "toggle": choice
        }
        return self.send_command(command)

    def trigger_special_action(self, index:int):
        command = {
            "action": "TriggerSpecialAction",
            "id": self.dev_name,
             "index": index
           }
        return self.send_command(command)
    
    def trigger_idle_anim(self, index:int):
        command = {
            "action": "SelectIdleAnim",
            "id": self.dev_name,
            "animName": index
        }
        return self.send_command(command)
    

    def trigger_emote(self, anim_name:str):
        command = {
            "action": "TriggerEmote",
            "id": self.dev_name,
            "itemName": anim_name
        }
        return self.send_command(command)


    def trigger_pose(self, pose_index:int):
        command = {
            "action": "TriggerPose",
            "id": self.dev_name,
            "index": pose_index
        }
        return self.send_command(command)

    def get_scenes(self):
        command = { 
            "action": "GetScenes",
            "id": "MyDevName" 
        }
        return self.send_command(command)
    
    def get_quickscenes(self):
        command = { 
            "action": "GetQuickscenes",
            "id": "MyDevName" 
        }
        return self.send_command(command)

    def load_scene(self, scene_name:str):
        command = {
            "action": "LoadScene",
            "id": self.dev_name,
            "name": scene_name
        }
        return self.send_command(command)
    

    def load_quick_scene(self, scene_index:int):
        command = {
            "action": "LoadQuickscene",
            "id": self.dev_name,
            "index": scene_index
        }
        return self.send_command(command)
    

    def get_avatars(self):
        command = {
			"action": "GetAvatars",
			"id": self.dev_name
		}
        return self.send_command(command)
    
    def load_avatar(self, avatar_name:str):
        command = {
            "action": "LoadAvatar",
            "id": self.dev_name,
            "name": avatar_name
        }
        return self.send_command(command)
    

    def cross_eyes(self, choice:bool):
        command = {
            "action": "SetOverride",           
            "behavior": "Cross Eyes",            
            "value": choice
        }
        return self.send_command(command)

    def auto_blink(self, choice:bool, frequency:float):
        command = {
            "action": "SetOverride",           
            "behavior": "Auto Blink",            
            "value": choice,
            "frequency": frequency
        }
        return self.send_command(command)
    
    def look_at_camera(self, choice:bool):
        command = {
            "action": "SetOverride",           
            "behavior": "Look At Camera",            
            "value": choice
            ## "range": 0.5
        }
        return self.send_command(command)
    

    def mousekeyboard_behavior(self, choice:bool, keyboardScale, handToKeyboardDist, xOffset, yOffset, zOffset):
        """ NO idea what this does or how to use it """

        command = {
            "action": "SetOverride",                    # required (string) 
            "behavior": "Mouse Keyboard Behavior",      # required (string)
            "value": choice,                            # required (bool)
            "keyboardScale": keyboardScale,             # optional (float)
            "handToKeyboardDist": handToKeyboardDist,   # optional (float)
            "xAxisOffset": xOffset,                     # optional (float)
            "yAxisOffset": yOffset,                     # optional (float)
            "zAxisOffset ": zOffset                     # optional (float)
        }
        return self.send_command(command)


    def follow_mouse(self, choice:bool):
        """ NO idea what this does or how to use it """
        command ={
            "action": "SetOverride",            # required (string) 
            "behavior": "Follow Mouse Cursor",  # required (string)
            "value": choice                     # required (bool)
        }
        return self.send_command(command)
    
    def pupil_behavoior(self, value, frequency:float=None):
        """ Adjust how often the pupils move 
            - value: True or False
            - frequency: 0.0 - 1.0
            """
        command = {
            "action": "SetOverride",          # required (string) 
            "behavior": "Pupil Behavior",     # required (string)
            "value": value,                   # required (bool)
            "frequency": frequency            # optional required (float)
        }
        return self.send_command(command)
    

    def breathing_behavior(self, value, amplitude:float, frequency:float):
        """ Doesnt appear to do much, but does work """
        command = {
            "action": "SetOverride",          # required (string) 
            "behavior": "Breathing Behavior", # required (string)
            "value": value,                   # required (bool)
            "amplitude": amplitude,           # optional required (float)
            "frequency": frequency            # optional required (float)
        }
        return self.send_command(command)
    


