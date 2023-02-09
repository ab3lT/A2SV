class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = sorted(collections.Counter(tasks).values())
        idles = (cnt[-1] - 1) * n
        for i in range(len(cnt) - 1): idles -= min(cnt[i], cnt[-1] - 1)
        return idles > 0 and idles + len(tasks) or len(tasks)