"""Rohonc Cartographia — CLI entry point."""

import argparse
from .navigator import lookup, list_pages, classify_regime


def main():
    parser = argparse.ArgumentParser(description='Rohonc Cartographia — topological regime classifier')
    sub = parser.add_subparsers(dest='command')

    p_lookup = sub.add_parser('lookup', help='Look up a page')
    p_lookup.add_argument('page', type=int, help='Page number (1-448)')

    p_list = sub.add_parser('list', help='List pages')
    p_list.add_argument('--regime', '-r', choices=['liturgical', 'pictographic_narrative', 'astronomical', 'mixed'],
                        help='Filter by regime')

    p_classify = sub.add_parser('classify', help='Classify a topological signature')
    p_classify.add_argument('--thorn', '-T', required=True, help='Þ value')
    p_classify.add_argument('--ring', '-R', required=True, help='Ř value')
    p_classify.add_argument('--gamma', '-G', required=True, help='ɢ value')
    p_classify.add_argument('--omega', '-O', required=True, help='Ω value')

    args = parser.parse_args()

    if args.command == 'lookup':
        result = lookup(args.page)
        print(f"Page {result['page']}: regime = {result['regime']}")
        print(f"  Description: {result['regime_description']}")
        print(f"  Bottleneck T: {result['bottleneck_primitives']['Þ']}")
        print(f"  Bottleneck R: {result['bottleneck_primitives']['Ř']}")
        print(f"  Bottleneck G: {result['bottleneck_primitives']['ɢ']}")
        print(f"  Bottleneck Omega: {result['bottleneck_primitives']['Ω']}")

    elif args.command == 'list':
        pages = list_pages(args.regime)
        regime_counts = {}
        for p in pages:
            regime_counts[p['regime']] = regime_counts.get(p['regime'], 0) + 1
        print(f"Pages: {len(pages)}")
        for regime, count in sorted(regime_counts.items()):
            print(f"  {regime}: {count} pages")

    elif args.command == 'classify':
        sig = {'Þ': args.thorn, 'Ř': args.ring, 'ɢ': args.gamma, 'Ω': args.omega}
        result = classify_regime(sig)
        print(f"Classification: {result['classification']}")
        print(f"Confidence: {result['confidence']:.3f}")
        print(f"Description: {result['description']}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
