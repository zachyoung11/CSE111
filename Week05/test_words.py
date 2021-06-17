from words import prefix, suffix
import pytest

def test_prefix():
   assert "" == prefix("","")
   assert "" == prefix("","correct")
   assert "" == prefix("clear", "")
   assert "" == prefix("happy", "funny")
   assert "cat" == prefix("cat", "catalog")
   assert "dog" == prefix("dogmatic", "dog")
   assert "j" == prefix("jump", "joyous")
   assert "un" == prefix("unwise", "ungrateful")
   assert "dis" == prefix("Disable", "distasteful")




pytest.main(["-v", "--tb=line", "-rN", "test_words.py"]) 
