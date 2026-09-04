from client import CodebaseInvariantAssertionSentinelClient

def main():
    client = CodebaseInvariantAssertionSentinelClient()
    res = client.verify_patch_invariants('diff --git ...', ['STDLIB_ONLY'])
    print('Invariant Sentinel: ' + res['sentinel_id'] + ' (' + res['governance_verdict'] + ')')
    print('Preserved: ' + str(res['all_invariants_preserved']) + ' | Evaluated: ' + str(res['invariants_evaluated']))
    print('Audit URL: ' + res['sentinel_audit_url'])

if __name__ == '__main__':
    main()
