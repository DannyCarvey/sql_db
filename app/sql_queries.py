MAKE_SPELL_TABLE = '''
CREATE TABLE IF NOT EXISTS spells
(
"name" VARCHAR(30) NOT NULL,
"source" VARCHAR(50) NOT NULL,
"spell_level" VARCHAR(15) NOT NULL,
"school" VARCHAR(30) NOT NULL,
"ritual" Boolean NOT NULL,
"casting_time" VARCHAR(150) NOT NULL,
"range" VARCHAR(30) NOT NULL,
"components" VARCHAR(150) NOT NULL,
"duration" VARCHAR(50) NOT NULL,
"concentration" Boolean NOT NULL,
"desc" VARCHAR(5000) NOT NULL,
"at_higher_levels" VARCHAR(500) NOT NULL,
"spell_lists" VARCHAR(300) NOT NULL
);
'''

INSERT_SPELL = "INSERT INTO spells VALUES (:name, 'Source:source', :spell_level, :school, :ritual, 'Casting Time:casting_time', 'Range:range', 'Components:components', 'Duration:duration', 'Concentration:concentration', :desc, 'At Higher Levels:at_higher_levels', 'Spell Lists:spell_lists')"

DROP_SPELL_TABLE = '''
DROP TABLE IF EXISTS spells
'''
