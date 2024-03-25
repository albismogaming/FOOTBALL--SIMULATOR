import numpy as np
import sys
import os
from scipy.stats import norm
from SIM_FUNCTIONS import *

class Play:
    def __init__(self, game_state):
        self.game_state = game_state

    def run(self):
        if self.game_state.down == 1:
            rush_yds = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            probs = np.array([0.00410393830377583, 0.0965374998681254, 0.559322480930929, 0.232742886682773, 0.0596337050439406, 0.0231993838817559, 0.0101543460601137, 0.00496903583824786, 0.00282211695696667, 0.00171437011404517, 0.00121324654224735, 0.000954772278899005, 0.000727947925348413, 0.00050112357179782, 0.000379798917573085, 0.000284849188179814, 0.000274299218247228, 0.000232099338516885, 0.000179349488853957, 5.27498496629285E-06, 4.21998797303428E-05, 5.27498496629285E-06])
            probs /= probs.sum()
            sel_bin = np.random.choice(len(rush_yds) - 1, p=probs)
            yards_gained = np.round(np.random.uniform(rush_yds[sel_bin], rush_yds[sel_bin + 1]))

        elif self.game_state.down == 2:
            rush_yds = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            probs = np.array([0.00423552515519164, 0.0961023183051242, 0.551350541714514, 0.234260322532328, 0.0667116015111422, 0.0239735716544344, 0.00957777888728011, 0.00503436683475627, 0.00266280559854877, 0.00181403631401135, 0.00121490505433788, 0.000840448017041956, 0.000499276049727895, 0.0004743122472415, 0.000432705909764175, 0.000316208164827667, 0.000199710419891158, 0.000133140279927439, 0.000091533942450114, 2.49638024863947E-05, 4.16063374773245E-05, 8.32126749546491E-06])
            probs /= probs.sum()
            sel_bin = np.random.choice(len(rush_yds) - 1, p=probs)
            yards_gained = np.round(np.random.uniform(rush_yds[sel_bin], rush_yds[sel_bin + 1]))

        elif self.game_state.down == 3:
            rush_yds = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            probs = np.array([0.00481661732978777, 0.0822838793838744, 0.55862726406101, 0.214816115598816, 0.0811298981486127, 0.0293512618533942, 0.0126436204906929, 0.00582007927349355, 0.00321107821985851, 0.00240830866489388, 0.00135467362400281, 0.000827856103557273, 0.000752596457779339, 0.000702423360594049, 0.000401384777482314, 0.000301038583111735, 0.000225778937333802, 0.000150519291555868, 5.01730971852893E-05, 5.01730971852893E-05, 5.01730971852893E-05, 2.50865485926446E-05])
            probs /= probs.sum()
            sel_bin = np.random.choice(len(rush_yds) - 1, p=probs)
            yards_gained = np.round(np.random.uniform(rush_yds[sel_bin], rush_yds[sel_bin + 1]))

        elif self.game_state.down == 4:
            rush_yds = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            probs = np.array([0.0143430866322433, 0.0847198317077835, 0.697647733792312, 0.112449799196787, 0.0407343660355709, 0.0179766685790782, 0.0101357812201186, 0.00688468158347676, 0.00516351118760757, 0.00286861732644865, 0.00229489386115892, 0.00133868808567604, 0.00133868808567604, 0.00057372346528973, 0.000191241155096577, 0.000191241155096577, 0.000191241155096577, 0.000191241155096577, 0.000191241155096577, 0.000191241155096577, 0.000191241155096577, 0.000191241155096577])
            probs /= probs.sum()
            sel_bin = np.random.choice(len(rush_yds) - 1, p=probs)
            yards_gained = np.round(np.random.uniform(rush_yds[sel_bin], rush_yds[sel_bin + 1]))

        SimFunctions.scroll_print("THEY HAND IT OFF!")
        SimFunctions.scroll_print(f"YARDS GAINED: {yards_gained}")
        return yards_gained
    
    def short_pass(self):
        sh_yds = np.array([1, 3, 6, 9])
        sh_prob = np.array([0.333834665, 0.43583058, 0.230334754])
        sh_prob /= sh_prob.sum()

        if self.game_state.down == 1:
            sh_cp = np.array([0.753965104, 0.732654343, 0.659118611])
            sh_std = np.array([0.093170671, 0.091607139, 0.09864751])
            sh_int = 0.0166227727389154


            yac_avg = np.array([4.982616327, 3.6174632, 3.11295076])
            yac_std = np.array([5.229968676, 4.640117864, 4.482464224])
        
        elif self.game_state.down == 2:
            sh_cp = np.array([0.743354823, 0.716364507, 0.647100539])
            sh_std = np.array([0.094823477, 0.098672484, 0.10071221])
            sh_int = 0.0166227727389154

            yac_avg = np.array([4.753357408, 3.445257091, 3.141473402])
            yac_std = np.array([5.276543318, 4.511373735, 4.718899122])

        elif self.game_state.down == 3:
            sh_cp = np.array([0.701618172, 0.65992684, 0.589101564])
            sh_std = np.array([0.102791736, 0.105879433, 0.098694407])
            sh_int = 0.0166227727389154

            yac_avg = np.array([5.107097314, 4.073152032, 3.40707681])
            yac_std = np.array([5.698118718, 5.569732659, 5.171714554])

        elif self.game_state.down == 4:
            sh_cp = np.array([0.640995029, 0.635643645, 0.584497972])
            sh_std = np.array([0.116653604, 0.119014828, 0.10665217])
            sh_int = 0.0166227727389154

            yac_avg = np.array([3.764830299, 4.002855625, 3.674758251])
            yac_std = np.array([4.828401637, 5.713351666, 5.089617448])


        sel_bin = np.random.choice(len(sh_yds) - 1, p=sh_prob)
        sel_cp, sel_std, sel_int = sh_cp[sel_bin], sh_std[sel_bin], sh_int
        sel_yavg, sel_ystd = yac_avg[sel_bin], yac_std[sel_bin]        

        success_prob = np.round(np.random.normal(loc=sel_cp, scale=sel_std), 4)
        pass_yds = np.round(np.random.uniform(sh_yds[sel_bin], sh_yds[sel_bin + 1]))

        yac_gained = np.random.normal(loc=sel_yavg, scale=sel_ystd)
        yac_gained = np.round(yac_gained)
        yac_gained = max(yac_gained, -3)
        yards_gained = pass_yds + yac_gained
        interception = False
        incompletion = False

        SimFunctions.scroll_print(f"COMP%: {success_prob}")
        SimFunctions.scroll_print(f"AIR YARDS: {pass_yds}")

        if np.random.rand() <= success_prob:
            SimFunctions.scroll_print("PASS IS COMPLETED!")
            SimFunctions.scroll_print(f"YDS AFTER CATCH: {yac_gained}")
            SimFunctions.scroll_print(f"YARDS GAINED: {yards_gained}")
        else:
            if np.random.rand() <= sel_int:
                    interception = True
                    SimFunctions.scroll_print("PASS IS INTERCEPTED!")
                    yards_gained = pass_yds
            else:
                SimFunctions.scroll_print("PASS FALLS INCOMPLETE!")
                incompletion = True
                yards_gained = int(0)

        return yards_gained, interception, incompletion
  
    def medium_pass(self):
        md_yds = np.array([10, 14, 19, 24])
        md_prob = np.array([0.48987, 0.33832, 0.17181])
        md_prob /= md_prob.sum()

        if self.game_state.down == 1:
            md_cp = np.array([0.59778, 0.55501, 0.43370])
            md_std = np.array([0.0998559710283904, 0.102041677940287, 0.0797641352311969])
            md_int = 0.0418952268447584

            yac_avg = np.array([3.4797380261566, 4.27653945046787, 5.06955002515426])
            yac_std = np.array([5.12599307610936, 5.80500655957421, 5.87247609209133])
        
        elif self.game_state.down == 2:
            md_cp = np.array([0.590134160805344, 0.527687914191298, 0.411552519610334])
            md_std = np.array([0.103226106412874, 0.102885098724157, 0.0747293629854516])
            md_int = 0.0418952268447584

            yac_avg = np.array([3.26623480564153, 3.96818086536615, 5.36830281032892])
            yac_std = np.array([4.84512060273975, 5.24239873280357, 6.42643062281663])

        elif self.game_state.down == 3:
            md_cp = np.array([0.532282045570988, 0.477680804636985, 0.386197872676541])
            md_std = np.array([0.0992110477276905, 0.0979389468374606, 0.0686541691290926])
            md_int = 0.0418952268447584

            yac_avg = np.array([3.20457104757421, 3.81775717480807, 5.30401161918378])
            yac_std = np.array([4.96507160958752, 5.08679902359473, 6.15630330332864])

        elif self.game_state.down == 4:
            md_cp = np.array([0.52011738248703, 0.447551725128522, 0.349015120304265])
            md_std = np.array([0.103986901935966, 0.0992875761381089, 0.0654694406323929])
            md_int = 0.0418952268447584

            yac_avg = np.array([3.94634255264675, 3.74444681392867, 3.35556818181818])
            yac_std = np.array([5.50434318932932, 4.43331930999059, 3.91882570265124])

        sel_bin = np.random.choice(len(md_yds) - 1, p=md_prob)
        sel_cp, sel_std, sel_int = md_cp[sel_bin], md_std[sel_bin], md_int
        sel_yavg, sel_ystd = yac_avg[sel_bin], yac_std[sel_bin]        

        success_prob = np.round(np.random.normal(loc=sel_cp, scale=sel_std), 4)
        pass_yds = np.round(np.random.uniform(md_yds[sel_bin], md_yds[sel_bin + 1]))

        yac_gained = np.random.normal(loc=sel_yavg, scale=sel_ystd)
        yac_gained = np.round(yac_gained)
        yac_gained = max(yac_gained, -3)
        yards_gained = pass_yds + yac_gained
        interception = False
        incompletion = False

        SimFunctions.scroll_print(f"COMP%: {success_prob}")
        SimFunctions.scroll_print(f"AIR YARDS: {pass_yds}")

        if np.random.rand() <= success_prob:
            SimFunctions.scroll_print("PASS IS COMPLETED!")
            SimFunctions.scroll_print(f"YDS AFTER CATCH: {yac_gained}")
            SimFunctions.scroll_print(f"YARDS GAINED: {yards_gained}")
        else:
            if np.random.rand() <= sel_int:
                    interception = True
                    SimFunctions.scroll_print("PASS IS INTERCEPTED!")
                    yards_gained = pass_yds
            else:
                SimFunctions.scroll_print("PASS FALLS INCOMPLETE!")
                incompletion = True
                yards_gained = int(0)

        return yards_gained, interception, incompletion
    
    def deep_pass(self):
        dp_yds = np.array([25, 30, 35, 39])
        dp_prob = np.array([0.463989379356123, 0.304900984622193, 0.231109636021684])
        dp_prob /= dp_prob.sum()

        if self.game_state.down == 1:
            dp_cp = 0.320399792944273
            dp_std = 0.0389067725183367
            dp_int = 0.0664343400818675

            yac_avg = 7.00152238610743
            yac_std = 6.63779409592549
        
        elif self.game_state.down == 2:
            dp_cp = 0.309364196818913
            dp_std = 0.0385251563825337
            dp_int = 0.0664343400818675

            yac_avg = 6.56886277495534
            yac_std = 6.05746493494292

        elif self.game_state.down == 3:
            dp_cp = 0.315084566741358
            dp_std = 0.0417345640401138
            dp_int = 0.0664343400818675

            yac_avg = 7.2471383883541
            yac_std = 6.80413737732286

        elif self.game_state.down == 4:
            dp_cp = 0.244297396437484
            dp_std = 0.0422124536944304
            dp_int = 0.0664343400818675

            yac_avg = 3.63191919191919
            yac_std = 3.13136592017093

        sel_bin = np.random.choice(len(dp_yds) - 1, p=dp_prob)
        sel_cp, sel_std, sel_int = dp_cp, dp_std, dp_int
        sel_yavg, sel_ystd = yac_avg, yac_std        

        success_prob = np.round(np.random.normal(loc=sel_cp, scale=sel_std), 4)
        pass_yds = np.round(np.random.uniform(dp_yds[sel_bin], dp_yds[sel_bin + 1]))
        
        yac_gained = np.random.normal(loc=sel_yavg, scale=sel_ystd)
        yac_gained = np.round(yac_gained)
        yac_gained = max(yac_gained, -3)
        yards_gained = pass_yds + yac_gained
        interception = False
        incompletion = False

        SimFunctions.scroll_print(f"COMP%: {success_prob}")
        SimFunctions.scroll_print(f"AIR YARDS: {pass_yds}")

        if np.random.rand() <= success_prob:
            SimFunctions.scroll_print("PASS IS COMPLETED!")
            SimFunctions.scroll_print(f"YDS AFTER CATCH: {yac_gained}")
            SimFunctions.scroll_print(f"YARDS GAINED: {yards_gained}") 
        else:
            if np.random.rand() <= sel_int:
                    interception = True
                    SimFunctions.scroll_print("PASS IS INTERCEPTED!")
                    yards_gained = pass_yds
            else:
                SimFunctions.scroll_print("PASS FALLS INCOMPLETE!")
                incompletion = True
                yards_gained = int(0)

        return yards_gained, interception, incompletion

    def bomb_pass(self):
        bb_yds = np.array([40, 50, 60, 70])
        bb_prob = np.array([0.828461666945048, 0.164356104893937, 0.00718222816101553])
        bb_prob /= bb_prob.sum()

        if self.game_state.down == 1:
            bb_cp = 0.290496074749622
            bb_std = 0.0387162755910165
            bb_int = 0.0923667947218974

            yac_avg = 6.55995327301808
            yac_std = 5.5112682938495
        
        elif self.game_state.down == 2:
            bb_cp = 0.266429551583442
            bb_std = 0.0387162755910165
            bb_int = 0.0923667947218974

            yac_avg = 5.60956408649799
            yac_std = 4.23027591191699

        elif self.game_state.down == 3:
            bb_cp = 0.280498920166539
            bb_std = 0.0387162755910165
            bb_int = 0.0923667947218974

            yac_avg = 6.91974972095262
            yac_std = 5.34686045095062

        elif self.game_state.down == 4:
            bb_cp = 0.199301044488775
            bb_std = 0.0387162755910165
            bb_int = 0.0923667947218974

            yac_avg = 3.71666666666667
            yac_std = 2.09598693510419

        sel_bin = np.random.choice(len(bb_yds) - 1, p=bb_prob)
        sel_cp, sel_std, sel_int = bb_cp, bb_std, bb_int
        sel_yavg, sel_ystd = yac_avg, yac_std        

        success_prob = np.round(np.random.normal(loc=sel_cp, scale=sel_std), 4)
        pass_yds = np.round(np.random.uniform(bb_yds[sel_bin], bb_yds[sel_bin + 1]))
        
        yac_gained = np.random.normal(loc=sel_yavg, scale=sel_ystd)
        yac_gained = np.round(yac_gained)
        yac_gained = max(yac_gained, -3)
        yards_gained = pass_yds + yac_gained
        interception = False
        incompletion = False

        SimFunctions.scroll_print(f"COMP%: {success_prob}")
        SimFunctions.scroll_print(f"AIR YARDS: {pass_yds}")

        if np.random.rand() <= success_prob:
            SimFunctions.scroll_print("PASS IS COMPLETED!")
            SimFunctions.scroll_print(f"YDS AFTER CATCH: {yac_gained}")
            SimFunctions.scroll_print(f"YARDS GAINED: {yards_gained}") 
        else:
            if np.random.rand() <= sel_int:
                    interception = True
                    SimFunctions.scroll_print("PASS IS INTERCEPTED!")
                    yards_gained = pass_yds
            else:
                SimFunctions.scroll_print("PASS FALLS INCOMPLETE!")
                incompletion = True
                yards_gained = int(0)

        return yards_gained, interception, incompletion

    def punt(self):
        blocked_options = np.array(["BLOCKED", "PUNTED"])
        block_probs = np.array([0.0054035744241564, 0.994596425575844])
        block_choice = np.random.choice(blocked_options, p=block_probs)

        if block_choice == "BLOCKED":
            sptm_result = "BLOCKED"
            yards_gained = int(np.random.random(-15, 0))
            SimFunctions.scroll_print("THE PUNT IS BLOCKED!!!!")
            SimFunctions.scroll_print(f"YARDS PUNTED: {yards_gained}")
            return yards_gained
        else:
            ret_outcome = np.array(["OB", "DN", "FC", "RT"])
            ret_probs = np.array([0.0938518674689025, 0.135336760675305, 0.233648497429494, 0.537162874426299])
            sptm_result = np.random.choice(ret_outcome, p=ret_probs)
    
            punt_yds = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
            probs = np.array([0.00120020760347736, 0.00621188529907876, 0.0535227715064227, 0.248199688594784, 0.398923056961204, 0.247713117944726, 0.0409205916699105, 0.00308161411703646, 0.000210847281691968, 0.000016219021668613])
            probs /= probs.sum()
            sel_bin = np.random.choice(len(punt_yds) -1, p=probs)
            yards_gained = np.round(np.random.uniform(punt_yds[sel_bin], punt_yds[sel_bin + 1]))

            ret_yds = np.array([-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
            probs = np.array([0.0456192258921563, 0.646851035565485, 0.22655636736912, 0.044320995108991, 0.0152768552623634, 0.00679306805144617, 0.00413622365799167, 0.00320028983757019, 0.00332105549181813, 0.00295875852907433, 0.000966125233983455])
            probs /= probs.sum()
            sel_bin = np.random.choice(len(ret_yds) - 1, p=probs)
            yards_ret = np.round(np.random.uniform(ret_yds[sel_bin], ret_yds[sel_bin + 1]))

            if self.game_state.yardline + yards_gained >= 100:
                sptm_result = "TOUCHBACK"
                SimFunctions.scroll_print("PUNTED INTO THE ENDZONE FOR A TOUCHBACK!")
                SimFunctions.scroll_print(f"YARDS PUNTED: {yards_gained}")
                return yards_gained, sptm_result
            elif self.game_state.yardline + (yards_gained - yards_ret) <= 0:
                sptm_result = "RET TD"
                SimFunctions.scroll_print("PUNT RETURNED FOR TOUCHDOWN!")
                SimFunctions.scroll_print(f"YARDS PUNTED: {yards_gained}")
                SimFunctions.scroll_print(f"YARDS RETURNED: {yards_ret}")
            else: 
                if sptm_result == "OB":
                    yards_ret = int(0)
                    SimFunctions.scroll_print("PUNTED OUT OF BOUNDS!")
                    SimFunctions.scroll_print(f"YARDS PUNTED: {yards_gained}")
                elif sptm_result == "DN":
                    yards_ret = int(0)
                    SimFunctions.scroll_print("PUNT IS DOWNED!")
                    SimFunctions.scroll_print(f"YARDS PUNTED: {yards_gained}")
                elif sptm_result == "FC":
                    yards_ret = int(0)
                    SimFunctions.scroll_print("PUNT IS FAIR CAUGHT!")
                    SimFunctions.scroll_print(f"YARDS PUNTED: {yards_gained}")
                elif sptm_result == "RT":
                    SimFunctions.scroll_print("PUNT RETURNED")
                    SimFunctions.scroll_print(f"YARDS PUNTED: {yards_gained}")
                    SimFunctions.scroll_print(f"YARDS RETURNED: {yards_ret}")
                self.game_state.yardline += yards_gained - yards_ret
            return yards_gained, sptm_result

    def field_goal(self):
        fg_yds = np.array([17, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
        probabilities = np.array([0.985629626925428,0.98031366336069,0.959233525067658,0.923350559787532,0.874462159868896,0.805427724947955,0.727005326366539,0.637839529681707,0.518257127879043,0.350804819901275,0.232825814758255])
        stdev = np.array([0.00570197034643234,0.00805973904726757,0.0167325638616261,0.0283535956584111,0.0348187746944,0.0423739386339786,0.0478249535587302,0.0590887890525225,0.0737668874444816,0.0777332987791278,0.0205736561391044])

        distance = self.game_state.distance_to_goal()
        idx = np.abs(fg_yds - distance).argmin()
        selected_prob = probabilities[idx]
        selected_std = stdev[idx]

        modified_prob = np.round(np.random.normal(loc=selected_prob, scale=selected_std), 4)
        modified_prob = np.clip(modified_prob, 0, 1)
        
        sptm_result = None
        if np.random.rand() <= modified_prob:
            SimFunctions.scroll_print(f'DISTANCE: {distance} YDS')
            SimFunctions.scroll_print(f'SUCCESS PROB: {modified_prob}')
            SimFunctions.scroll_print('FIELD GOAL IS GOOD!')
            sptm_result = "GOOD"
        else:
            SimFunctions.scroll_print(f'DISTANCE: {distance} YDS')
            SimFunctions.scroll_print(f'SUCCESS PROB: {modified_prob}')
            SimFunctions.scroll_print("FIELD GOAL IS NO GOOD!")
            sptm_result = "NO GOOD"
        return sptm_result

    def extra_point(self):
        distance = 33
        expt_avg = 0.963723594
        expt_std = 0.023007936
        expt_prob = np.round(np.random.normal(loc=expt_avg, scale=expt_std), 4)
        expt_prob = np.clip(expt_prob, 0, 1)

        sptm_result = None
        if np.random.rand() <= expt_prob:
            SimFunctions.scroll_print(f'DISTANCE: {distance} YDS')
            SimFunctions.scroll_print(f'SUCCESS PROB: {expt_prob}')
            SimFunctions.scroll_print('EXTRA POINT IS UP AND GOOD!')
            sptm_result = "GOOD"
        else:
            SimFunctions.scroll_print(f'DISTANCE: {distance} YDS')
            SimFunctions.scroll_print(f'SUCCESS PROB: {expt_prob}')
            SimFunctions.scroll_print("EXTRA POINT IS NO GOOD!.")
            sptm_result = "NO GOOD"
        return sptm_result 
    
    def kickoff(self):
        tb_ret = np.array(["TOUCHBACK", "RETURNED"])
        tb_probs = np.array([0.383602070762027, 0.616397929237973])
        sptm_result = np.random.choice(tb_ret, p=tb_probs)

        if sptm_result == "TOUCHBACK":
            SimFunctions.scroll_print("KICK GOES THROUGH THE ENDZONE!")
            SimFunctions.scroll_print("---  TOUCHBACK!  ---")
            return 0, sptm_result
        elif sptm_result == "RETURNED":
            kick_dist = np.array([50, 55, 60, 65, 75])
            dist_probs = np.array([0.0298035783741735, 0.0942240373395566, 0.174202644885259, 0.701769739401011])
            dist_probs /= dist_probs.sum()
            sel_bin = np.random.choice(len(kick_dist) - 1, p=dist_probs)
            distance = np.round(np.random.uniform(kick_dist[sel_bin], kick_dist[sel_bin + 1]))

            ret_yards = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110])
            ret_probs = np.array([8.02654109589041E-05, 0.000802654109589041, 0.0136183647260274, 0.0238923373287671, 0.0900310359589041, 0.239164169520548, 0.293798159246575, 0.178884845890411, 0.0752622003424658, 0.0317315924657534, 0.0161868578767123, 0.0106485445205479, 0.0059396404109589, 0.00321061643835616, 0.00270226883561644, 0.0019263698630137, 0.00163206335616438, 0.00112371575342466, 0.00077589897260274, 0.00136451198630137, 0.00184610445205479, 0.00278253424657534, 0.0019798801369863, 0.000615368150684931])
            ret_probs /= ret_probs.sum()
            sel_bin = np.random.choice(len(ret_yards) - 1, p=ret_probs)
            yards_gained = np.round(np.random.uniform(ret_yards[sel_bin], ret_yards[sel_bin + 1]))

            if self.game_state.yardline + int(distance) >= 100:
                SimFunctions.scroll_print("DEEP KICK INTO THE ENDZONE!")
                SimFunctions.scroll_print(f"KICK DISTANCE: {distance} YDS")
                decision = input("TAKE A TOUCHBACK? (yes/no): ").lower().strip()
                if decision == "yes":
                    sptm_result = "TOUCHBACK"
                    SimFunctions.scroll_print("NO RETURN, TAKES A KNEE!")
                    SimFunctions.scroll_print("---  TOUCHBACK!  ---")
                    return 0, sptm_result
                elif (self.game_state.yardline + distance) - yards_gained <= 0:
                    sptm_result = "RET TD"
                    SimFunctions.scroll_print("KICK RETURNED FOR TOUCHDOWN!")
                    SimFunctions.scroll_print(f"YARDS RETURNED: {yards_gained}")
                else:
                    SimFunctions.scroll_print("RETURNER TAKES IT OUT!")
                    SimFunctions.scroll_print(f"YARDS RETURNED: {yards_gained}") 
                self.game_state.yardline += distance
                self.game_state.yardline -= 100 - yards_gained
            return yards_gained, sptm_result








    