class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "%%None%%"
        return "**%**".join(strs)
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        if s == "%%None%%":
            return []
        return s.split("**%**")