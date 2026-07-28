class Solution:
    hashcode={}
    def encode(self, strs: list[str]) -> str:
        key=hash(tuple(strs))
        self.hashcode[key]=strs
        return str(key)

    def decode(self, s: str) -> list[str]:
        return list(self.hashcode[int(s)])