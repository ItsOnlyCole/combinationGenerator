#!/usr/bin/env python3

from .context import combinationGenerator

generator = combinationGenerator.combinationGenerator.Generator(4, 9)
generator.generateCombinations()
