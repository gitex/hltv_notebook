import pytest
import pandas as pd

from infra.storage.factories import DataFrameFromCSVFactory
from infra.stubs import CSV


@pytest.fixture
def matches_df() -> pd.DataFrame:
    """ Returns a DataFrame with matches. """

    matches = CSV("""
    Date,Team1,Team2,Map,Event
    26/2/23,Budapest Five (5),Katuna (16),inf  Inferno,CCT South Europe Series 3
    26/2/23,Katuna (14),Budapest Five (16),anc  Ancient,CCT South Europe Series 3
    26/2/23,Budapest Five (12),Katuna (16),ovp  Overpass,CCT South Europe Series 3
    26/2/23,ECSTATIC (14),Astralis Talent (16),inf  Inferno,CCT North Europe Series 4 Closed Qualifier
    26/2/23,Eternal Fire (15),fnatic (19),ovp  Overpass,ESL Pro League Season 17
    26/2/23,fnatic (9),Eternal Fire (16),inf  Inferno,ESL Pro League Season 17
    26/2/23,SD Invicta (16),sYnck (14),inf  Inferno,Baltic Blastoff Spring 2023
    26/2/23,sYnck (16),SD Invicta (9),vtg  Vertigo,Baltic Blastoff Spring 2023
    26/2/23,SD Invicta (19),sYnck (17),mrg  Mirage,Baltic Blastoff Spring 2023
    26/2/23,Partizan (4),VOYVODA (16),mrg  Mirage,RES Season 4
    26/2/23,VOYVODA (16),Partizan (1),nuke  Nuke,RES Season 4
    26/2/23,Apeks Rebels (4),Websterz (16),anb  Anubis,CCT North Europe Series 4 Closed Qualifier
    26/2/23,Websterz (13),Apeks Rebels (16),ovp  Overpass,CCT North Europe Series 4 Closed Qualifier
    26/2/23,Apeks Rebels (13),Websterz (16),inf  Inferno,CCT North Europe Series 4 Closed Qualifier
    26/2/23,MCE (10),Permitta (16),mrg  Mirage,Polish Pro League AMA PRO Season 4
    26/2/23,Permitta (10),MCE (16),ovp  Overpass,Polish Pro League AMA PRO Season 4
    26/2/23,MCE (16),Permitta (19),nuke  Nuke,Polish Pro League AMA PRO Season 4
    26/2/23,Entropiq (16),MASONIC (13),vtg  Vertigo,CCT South Europe Series 3
    26/2/23,Entropiq (13),MASONIC (16),nuke  Nuke,CCT South Europe Series 3
    26/2/23,MASONIC (11),Entropiq (16),inf  Inferno,CCT South Europe Series 3
    26/2/23,HYDRA (11),ECSTATIC (16),ovp  Overpass,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,HYDRA (16),ECSTATIC (6),anc  Ancient,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,ECSTATIC (16),HYDRA (14),nuke  Nuke,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,HONORIS (16),Spirit Academy (14),inf  Inferno,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,Spirit Academy (16),HONORIS (5),nuke  Nuke,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,HONORIS (16),Spirit Academy (10),mrg  Mirage,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,ex-Rapid Ninjas (13),Apeks (16),anb  Anubis,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,Apeks (16),ex-Rapid Ninjas (12),inf  Inferno,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,SINNERS (8),1WIN (16),mrg  Mirage,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,1WIN (16),SINNERS (7),vtg  Vertigo,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,GenOne (7),Astralis Talent (16),vtg  Vertigo,CCT North Europe Series 4 Closed Qualifier
    26/2/23,GenOne (16),Astralis Talent (10),anb  Anubis,CCT North Europe Series 4 Closed Qualifier
    26/2/23,GenOne (12),Astralis Talent (16),inf  Inferno,CCT North Europe Series 4 Closed Qualifier
    26/2/23,iNation (16),Nexus (12),nuke  Nuke,RES Season 4
    26/2/23,Nexus (10),iNation (16),ovp  Overpass,RES Season 4
    26/2/23,iNation (9),Nexus (16),vtg  Vertigo,RES Season 4
    26/2/23,EC Brugge (6),Websterz (16),inf  Inferno,CCT North Europe Series 4 Closed Qualifier
    26/2/23,Websterz (16),EC Brugge (7),vtg  Vertigo,CCT North Europe Series 4 Closed Qualifier
    26/2/23,Cloud9 (16),Outsiders (8),anc  Ancient,ESL Pro League Season 17
    26/2/23,Cloud9 (14),Outsiders (16),mrg  Mirage,ESL Pro League Season 17
    26/2/23,Outsiders (9),Cloud9 (16),vtg  Vertigo,ESL Pro League Season 17
    26/2/23,500 (16),MOUZ NXT (14),mrg  Mirage,European Development Championship 7
    26/2/23,500 (16),MOUZ NXT (2),anc  Ancient,European Development Championship 7
    26/2/23,MOUZ NXT (16),500 (12),ovp  Overpass,European Development Championship 7
    26/2/23,Twisted Minds (16),Ooredoo Thunders (12),anb  Anubis,BLAST.tv Paris Major 2023 Middle East RMR Closed Qualifier
    26/2/23,Twisted Minds (16),Ooredoo Thunders (7),ovp  Overpass,BLAST.tv Paris Major 2023 Middle East RMR Closed Qualifier
    26/2/23,LDLC (13),1WIN (16),ovp  Overpass,ESL Challenger Melbourne 2023 Europe Open Qualifier
    26/2/23,ECLOT (16),Into the Breach (9),vtg  Vertigo,European Pro League Season 6
    26/2/23,Into the Breach (11),ECLOT (16),mrg  Mirage,European Pro League Season 6
    26/2/23,ECLOT (7),Into the Breach (16),inf  Inferno,European Pro League Season 6
    """)

    # Make a dataframe from matches
    return DataFrameFromCSVFactory()(matches)
