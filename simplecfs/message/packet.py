# -*- coding: utf-8 -*-
"""
define network packet
"""
import json

from simplecfs.common.parameters import OP_ADD_CHUNK, OP_ADD_CHUNK_REPLY,\
    OP_DELETE_CHUNK, OP_DELETE_CHUNK_REPLY, OP_GET_CHUNK, OP_GET_CHUNK_REPLY


def pack(data):
    """client pack the data to sending packet and return"""
    return json.dumps(data)


def unpack(packet):
    """ds unpack the data from received packet"""
    return json.loads(packet)


class AddChunkPacket(object):
    """
    define the add chunk packet
    """
    def __init__(self, chunk_id, chunk_length):
        """
        @chunk_id: the chunk id to be added
        @chunk_length: chunk data length
        """
        self._message = {}
        self._message['method'] = OP_ADD_CHUNK
        self._message['chunk_id'] = chunk_id
        self._message['length'] = chunk_length

    def get_message(self):
        """return add chunk packet message"""
        return self._message


class AddChunkReplyPacket(object):
    """add chunk reply packet"""
    def __init__(self, state, info=''):
        """
        @state: RET_FAILURE/RET_SUCCESS/etc.
        """
        self._message = {}
        self._message['method'] = OP_ADD_CHUNK_REPLY
        self._message['state'] = state
        self._message['info'] = info

    def get_message(self):
        """return add chunk packet message"""
        return self._message


class DeleteChunkPacket(object):
    """
    define the delete chunk packet
    """
    def __init__(self, chunk_id):
        """
        @chunk_id: the chunk id to be deleted
        """
        self._message = {}
        self._message['method'] = OP_DELETE_CHUNK
        self._message['chunk_id'] = chunk_id

    def get_message(self):
        """return add chunk packet message"""
        return self._message


class DeleteChunkReplyPacket(object):
    """delete chunk reply packet"""
    def __init__(self, state, info=''):
        """
        @state: RET_FAILURE/RET_SUCCESS/etc.
        """
        self._message = {}
        self._message['method'] = OP_DELETE_CHUNK_REPLY
        self._message['state'] = state
        self._message['info'] = info

    def get_message(self):
        """return add chunk packet message"""
        return self._message


class GetChunkPacket(object):
    """
    define the get chunk packet
    """
    def __init__(self, chunk_id, total_blocks, block_list):
        """
        @chunk_id: the chunk id to be get
        @total_blocks: total blocks in one chunk
        @block_list: block num to get(0,1,...,total_blocks-1)
        """
        self._message = {}
        self._message['method'] = OP_GET_CHUNK
        self._message['chunk_id'] = chunk_id
        self._message['total'] = total_blocks
        self._message['list'] = block_list

    def get_message(self):
        """return add chunk packet message"""
        return self._message


class GetChunkReplyPacket(object):
    """get chunk reply packet"""
    def __init__(self, state, info=''):
        """
        @state: RET_FAILURE/RET_SUCCESS/etc.
        """
        self._message = {}
        self._message['method'] = OP_GET_CHUNK_REPLY
        self._message['state'] = state
        self._message['info'] = info

    def get_message(self):
        """return get chunk packet message"""
        return self._message