# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:22:52 2021

@author: joshu
"""

import scrapy
from w3lib.html import remove_tags

class UniteScraper(scrapy.Spider):
    name = "unite"
    start_urls = ['https://www.pokemonunite.gg/guide']
    
    def parse(self, response):
        #this opens the page for each individual pokemon to scrape them 
        pokemon_pages = response.xpath('//div[@id="pkmnList"]//a')
        yield from response.follow_all(pokemon_pages, self.parse_pokemon)
        
    def parse_pokemon(self, response):
        #pokemon(response.xpath('.//h1/text()').get())
        for move in response.xpath('//div[@class="pkmn_move"]'):
            
            yield {
                'pokemon': response.xpath('.//h1/text()').get(),
                'name': move.xpath('./div[@class="move_title"]/h4/text()').get(),
                'effect': remove_tags(move.xpath('./p').get()),
                'upgrade': remove_tags(str(move.xpath('./p[@class="pkmn_move_plus_desc"]').get())),
                }
        
                        

        

    
    
        
