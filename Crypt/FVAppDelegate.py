#-*- coding: utf-8 -*-
#
#  Filevault_ServerAppDelegate.py
#  Filevault Server
#
#  Created by Graham Gilbert on 04/11/2012.
#
# Copyright 2013 Graham Gilbert.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from Foundation import *
import FVUtils
from AppKit import *

class FVAppDelegate(NSObject):
    def applicationWillFinishLaunching_(self, sender):
        # don't show menu bar
        NSMenu.setMenuBarVisible_(NO)

    def applicationDidFinishLaunching_(self, sender):
        # Prevent automatic relaunching at login on Lion
        if NSApp.respondsToSelector_('disableRelaunchOnLogin'):
            NSApp.disableRelaunchOnLogin()
        # Quit if filevault is already enabled, encrypting or decrypting.
        if FVUtils.filevaultStatus():
            NSApp.terminate_(self)
        # Quit if the server isn't available
        if not FVUtils.internet_on():
            NSApp.terminate_(self)
