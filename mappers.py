#!/usr/bin/python
# -*- coding: utf-8 -*-

emappers = {
        u'Henkilökulut': [u'salar[iy]',u'palkk[iao]',u'työkorvau',u'palkat',u'tuotanto',u'valmistelu'],
        u'Matkakulut' : [u'majoitus',u'matka',u'travel',u'transportation'],
        u'Kirjanpito': [u'book ?keeping',u'audit'],
        u'Rahoitus': [u'rahoitus',u'tuki',u'sponsor',u'payment',u'kumppanuus'],
        u'Tulot': [u'tulot',u'sales',u'hankeavustu'],
        u'Tilaisuudet': [u'tilaisuus',u'venue',u'rent',u'tilakust',u'tarjoilu',u'kiertue',u'tilavuokra',u'meeting',u'accommodation',u'hackathon',u'roadshow'],
        u'Hallinto': [u'mgmt',u'admin',u'hallinnointi'],
        u'Sisäiset siirrot': [u'yleiskulut',u'OKFFI-laina',u'OKF-koordinointi',u'OKFFIn hallinnointi',u'loans',u'jälkityöprojektit',u'seed funding',u'leftover',u'Refunds from projects',u'hanke',u'projekti'],
        u'Pankkikulut': [u'Service fees'],
        u'Palvelut': [u'IT.*domains'],
        u'Alihankinta': [u'alihankinta'],
        u'Ostot': [u'purchase',u'muut.*kulut',u'other costs',u'other expen[cs]es',u'materiaalikulu'],
        u'Muut kulut': [u'expenses'],
        u'Viestintä': [u'paino',u'tiedotus',u'verkkosivu',u'Markkinointi'],
        u'Tase': [u'avaussaldo',u'tase'],
        u'Työryhmät': [u'working groups',],
        u'Annetut apurahat': [u'kierroksen työpaketteihin',],
        u'Yleiset': [u'yleiskategoria',u'uncategorised',],
        }
