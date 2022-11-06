#
# Copyright 2022 CoolJWB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import time as tm;import mpmath as mp;s=tm.time();mp.mp.dps=314; ###############
a,b=mp.mpf(1),mp.fdiv(1,mp.sqrt(2));d=mp.mpf(.25);p=lambda n:mp.nprint(a*a/d,n)#
for n in range(8):x=(mp.fdiv(a+b,2),mp.sqrt(a*b));y=x[0]-a;d-=y**2*2**n;a,b=x  #
p(314);t=lambda:print(f" in {(tm.time()-s)*1000.0:.1f}ms.");t() ################
                    #########                 ##########
                    #########                 ##########
                    #########                 #########
                    #########                 ########
                    #########                 ########
                    #########                 ########
                    #########                 ########
                    #########                 ########
                    #########                 ########
                    #########                 ########
                    #########                 #########
                    #########                 #########
                    #########                 ##########
                    #########                 ##########
                  ##########                  ##########
                ############                  ##########
                ##########                    ##########                ####
              ############                    ############              ####
            ##############                      ############################
          ##############                        ##########################
          ##############                          ######################
          ############                              ##################