import json


def write_json_file(output_dict: dict) -> None:
    with open("output.txt", "w", encoding="utf-8") as write_file:
        json.dump(output_dict, write_file, ensure_ascii=False, indent=4)


def write_txt_file(output_dict: dict) -> None:
    with open("output.txt", "w", encoding="utf-8") as write_file:
        write_file.write(str(output_dict))


def main():
    count_json = int(input())
    offers_list = []
    while count_json:
        json_str = json.loads(input())
        for offer in json_str['offers']:
            # offers_list.append(offer)
            offers_list.append(
                {'market_sku': offer['market_sku'], 'offer_id': offer['offer_id'], 'price': offer['price']})
        count_json -= 1
    offers_list.sort(key=lambda x: (x['price'], x['offer_id']))
    write_json_file({'offers': offers_list})
    # write_txt_file({'offers': offers_list})
    # print({'offers': offers_list})


if __name__ == '__main__':
    main()

'''
3
{"offers": [{"offer_id": "offer1", "market_sku": 10846332, "price": 1490}, {"offer_id": "offer2", "market_sku": 682644, "price": 499}]}
{"offers": [{"offer_id": "offer4", "market_sku": 832784, "price": 14000}]}
{"offers": [{"offer_id": "offer3", "market_sku": 832784, "price": 14000}]}

'''
