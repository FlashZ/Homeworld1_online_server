from __future__ import annotations

import asyncio

import titan_binary_gateway


def test_parse_mini_routing_reconnect_client() -> None:
    clear = bytes(
        [
            titan_binary_gateway.MINI_HEADER_TYPE,
            titan_binary_gateway.MINI_ROUTING_SERVICE,
            titan_binary_gateway.ROUTING_RECONNECT_CLIENT,
            0x34,
            0x12,
            0x01,
        ]
    )

    parsed = titan_binary_gateway._parse_mini_routing_reconnect_client(clear)

    assert parsed == {
        "client_id": 0x1234,
        "want_missed_messages": True,
    }


def test_claim_pending_reconnect_by_id_requires_matching_ip() -> None:
    server = titan_binary_gateway.SilencerRoutingServer()
    server._pending_reconnects[7] = titan_binary_gateway.PendingNativeReconnect(
        client_id=7,
        client_name_raw=b"Alpha",
        client_name="Alpha",
        client_ip="1.2.3.4",
        client_ip_u32=0,
        connected_at=100.0,
        last_activity_at=101.0,
        last_activity_kind="peer_data",
        chat_count=1,
        peer_data_messages=2,
        peer_data_bytes=64,
    )

    missing = asyncio.run(server._claim_pending_reconnect_by_id(7, "9.9.9.9"))
    found = asyncio.run(server._claim_pending_reconnect_by_id(7, "1.2.3.4"))

    assert missing is None
    assert found is not None
    assert found.client_id == 7
    assert 7 not in server._pending_reconnects
