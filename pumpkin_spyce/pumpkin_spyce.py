"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import time

class NoSpice(Exception):
    def __init__(self):
        print "NoSpice Exception"

def pumpkin_spice(amount=1):
    def wrap(c):
        class ps_class(c):
            def __init__(self, *args, **kwargs):
                #Prevent false advertisting
                if (amount <= 0):
                    raise NoSpice()
                #Adding extra cost to constructing object
                time.sleep(amount)
                super(ps_class,self).__init__(*args, **kwargs)
        return ps_class
    return wrap
