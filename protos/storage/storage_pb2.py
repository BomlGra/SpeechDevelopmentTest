# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storage.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstorage.proto\x12\x06protos\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x9f\x01\n\x06Report\x12\x16\n\x0ephonetic_score\x18\x01 \x01(\x05\x12\x15\n\rgrammar_score\x18\x02 \x01(\x05\x12\x17\n\x0fvocabular_score\x18\x03 \x01(\x05\x12\x1d\n\x15\x63oherent_speech_score\x18\x04 \x01(\x05\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"-\n\x08Question\x12\x13\n\x0bquestion_id\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\"O\n\x05\x41udio\x12\x12\n\nattempt_id\x18\x01 \x01(\x05\x12\x13\n\x0bquestion_id\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12\x0c\n\x04path\x18\x04 \x01(\t\";\n\x14GetQuestionsResponse\x12#\n\tquestions\x18\x01 \x03(\x0b\x32\x10.protos.Question\",\n\x19GetReportsByUserIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"=\n\x1aGetReportsByUserIdResponse\x12\x1f\n\x07reports\x18\x01 \x03(\x0b\x32\x0e.protos.Report\"2\n\x12UploadAudioRequest\x12\x1c\n\x05\x61udio\x18\x01 \x01(\x0b\x32\r.protos.Audio\"\'\n\x13UploadAudioResponse\x12\x10\n\x08\x61udio_id\x18\x01 \x01(\x05\"&\n\x13StartAttemptRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"*\n\x14StartAttemptResponse\x12\x12\n\nattempt_id\x18\x01 \x01(\x05\"R\n\x1c\x41ttachReportToAttemptRequest\x12\x12\n\nattempt_id\x18\x01 \x01(\x05\x12\x1e\n\x06report\x18\x02 \x01(\x0b\x32\x0e.protos.Report\"/\n\x19GetReportByAttemptRequest\x12\x12\n\nattempt_id\x18\x01 \x01(\x05\"<\n\x1aGetReportByAttemptResponse\x12\x1e\n\x06report\x18\x01 \x01(\x0b\x32\x0e.protos.Report\"0\n\x1aGetAudiousInArchiveRequest\x12\x12\n\nattempt_id\x18\x01 \x01(\x05\".\n\x1bGetAudiousInArchiveResponse\x12\x0f\n\x07\x61rchive\x18\x01 \x01(\x0c\x32\xf6\x03\n\x07Storage\x12\x44\n\x0cGetQuestions\x12\x16.google.protobuf.Empty\x1a\x1c.protos.GetQuestionsResponse\x12I\n\x0cStartAttempt\x12\x1b.protos.StartAttemptRequest\x1a\x1c.protos.StartAttemptResponse\x12\x46\n\x0bUploadAudio\x12\x1a.protos.UploadAudioRequest\x1a\x1b.protos.UploadAudioResponse\x12U\n\x15\x41ttachReportToAttempt\x12$.protos.AttachReportToAttemptRequest\x1a\x16.google.protobuf.Empty\x12[\n\x12GetReportByAttempt\x12!.protos.GetReportByAttemptRequest\x1a\".protos.GetReportByAttemptResponse\x12^\n\x13GetAudiousInArchive\x12\".protos.GetAudiousInArchiveRequest\x1a#.protos.GetAudiousInArchiveResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_REPORT = _descriptor.Descriptor(
  name='Report',
  full_name='protos.Report',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phonetic_score', full_name='protos.Report.phonetic_score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grammar_score', full_name='protos.Report.grammar_score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vocabular_score', full_name='protos.Report.vocabular_score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coherent_speech_score', full_name='protos.Report.coherent_speech_score', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='protos.Report.created_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=247,
)


_QUESTION = _descriptor.Descriptor(
  name='Question',
  full_name='protos.Question',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='question_id', full_name='protos.Question.question_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='protos.Question.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=294,
)


_AUDIO = _descriptor.Descriptor(
  name='Audio',
  full_name='protos.Audio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempt_id', full_name='protos.Audio.attempt_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='question_id', full_name='protos.Audio.question_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='protos.Audio.content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='protos.Audio.path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=375,
)


_GETQUESTIONSRESPONSE = _descriptor.Descriptor(
  name='GetQuestionsResponse',
  full_name='protos.GetQuestionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='questions', full_name='protos.GetQuestionsResponse.questions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=436,
)


_GETREPORTSBYUSERIDREQUEST = _descriptor.Descriptor(
  name='GetReportsByUserIdRequest',
  full_name='protos.GetReportsByUserIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='protos.GetReportsByUserIdRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=482,
)


_GETREPORTSBYUSERIDRESPONSE = _descriptor.Descriptor(
  name='GetReportsByUserIdResponse',
  full_name='protos.GetReportsByUserIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reports', full_name='protos.GetReportsByUserIdResponse.reports', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=545,
)


_UPLOADAUDIOREQUEST = _descriptor.Descriptor(
  name='UploadAudioRequest',
  full_name='protos.UploadAudioRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='protos.UploadAudioRequest.audio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=597,
)


_UPLOADAUDIORESPONSE = _descriptor.Descriptor(
  name='UploadAudioResponse',
  full_name='protos.UploadAudioResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_id', full_name='protos.UploadAudioResponse.audio_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=638,
)


_STARTATTEMPTREQUEST = _descriptor.Descriptor(
  name='StartAttemptRequest',
  full_name='protos.StartAttemptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='protos.StartAttemptRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=678,
)


_STARTATTEMPTRESPONSE = _descriptor.Descriptor(
  name='StartAttemptResponse',
  full_name='protos.StartAttemptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempt_id', full_name='protos.StartAttemptResponse.attempt_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=722,
)


_ATTACHREPORTTOATTEMPTREQUEST = _descriptor.Descriptor(
  name='AttachReportToAttemptRequest',
  full_name='protos.AttachReportToAttemptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempt_id', full_name='protos.AttachReportToAttemptRequest.attempt_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report', full_name='protos.AttachReportToAttemptRequest.report', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=806,
)


_GETREPORTBYATTEMPTREQUEST = _descriptor.Descriptor(
  name='GetReportByAttemptRequest',
  full_name='protos.GetReportByAttemptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempt_id', full_name='protos.GetReportByAttemptRequest.attempt_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=808,
  serialized_end=855,
)


_GETREPORTBYATTEMPTRESPONSE = _descriptor.Descriptor(
  name='GetReportByAttemptResponse',
  full_name='protos.GetReportByAttemptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='report', full_name='protos.GetReportByAttemptResponse.report', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=857,
  serialized_end=917,
)


_GETAUDIOUSINARCHIVEREQUEST = _descriptor.Descriptor(
  name='GetAudiousInArchiveRequest',
  full_name='protos.GetAudiousInArchiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempt_id', full_name='protos.GetAudiousInArchiveRequest.attempt_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=919,
  serialized_end=967,
)


_GETAUDIOUSINARCHIVERESPONSE = _descriptor.Descriptor(
  name='GetAudiousInArchiveResponse',
  full_name='protos.GetAudiousInArchiveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='archive', full_name='protos.GetAudiousInArchiveResponse.archive', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=969,
  serialized_end=1015,
)

_REPORT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETQUESTIONSRESPONSE.fields_by_name['questions'].message_type = _QUESTION
_GETREPORTSBYUSERIDRESPONSE.fields_by_name['reports'].message_type = _REPORT
_UPLOADAUDIOREQUEST.fields_by_name['audio'].message_type = _AUDIO
_ATTACHREPORTTOATTEMPTREQUEST.fields_by_name['report'].message_type = _REPORT
_GETREPORTBYATTEMPTRESPONSE.fields_by_name['report'].message_type = _REPORT
DESCRIPTOR.message_types_by_name['Report'] = _REPORT
DESCRIPTOR.message_types_by_name['Question'] = _QUESTION
DESCRIPTOR.message_types_by_name['Audio'] = _AUDIO
DESCRIPTOR.message_types_by_name['GetQuestionsResponse'] = _GETQUESTIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetReportsByUserIdRequest'] = _GETREPORTSBYUSERIDREQUEST
DESCRIPTOR.message_types_by_name['GetReportsByUserIdResponse'] = _GETREPORTSBYUSERIDRESPONSE
DESCRIPTOR.message_types_by_name['UploadAudioRequest'] = _UPLOADAUDIOREQUEST
DESCRIPTOR.message_types_by_name['UploadAudioResponse'] = _UPLOADAUDIORESPONSE
DESCRIPTOR.message_types_by_name['StartAttemptRequest'] = _STARTATTEMPTREQUEST
DESCRIPTOR.message_types_by_name['StartAttemptResponse'] = _STARTATTEMPTRESPONSE
DESCRIPTOR.message_types_by_name['AttachReportToAttemptRequest'] = _ATTACHREPORTTOATTEMPTREQUEST
DESCRIPTOR.message_types_by_name['GetReportByAttemptRequest'] = _GETREPORTBYATTEMPTREQUEST
DESCRIPTOR.message_types_by_name['GetReportByAttemptResponse'] = _GETREPORTBYATTEMPTRESPONSE
DESCRIPTOR.message_types_by_name['GetAudiousInArchiveRequest'] = _GETAUDIOUSINARCHIVEREQUEST
DESCRIPTOR.message_types_by_name['GetAudiousInArchiveResponse'] = _GETAUDIOUSINARCHIVERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Report = _reflection.GeneratedProtocolMessageType('Report', (_message.Message,), {
  'DESCRIPTOR' : _REPORT,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.Report)
  })
_sym_db.RegisterMessage(Report)

Question = _reflection.GeneratedProtocolMessageType('Question', (_message.Message,), {
  'DESCRIPTOR' : _QUESTION,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.Question)
  })
_sym_db.RegisterMessage(Question)

Audio = _reflection.GeneratedProtocolMessageType('Audio', (_message.Message,), {
  'DESCRIPTOR' : _AUDIO,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.Audio)
  })
_sym_db.RegisterMessage(Audio)

GetQuestionsResponse = _reflection.GeneratedProtocolMessageType('GetQuestionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETQUESTIONSRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetQuestionsResponse)
  })
_sym_db.RegisterMessage(GetQuestionsResponse)

GetReportsByUserIdRequest = _reflection.GeneratedProtocolMessageType('GetReportsByUserIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTSBYUSERIDREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetReportsByUserIdRequest)
  })
_sym_db.RegisterMessage(GetReportsByUserIdRequest)

GetReportsByUserIdResponse = _reflection.GeneratedProtocolMessageType('GetReportsByUserIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTSBYUSERIDRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetReportsByUserIdResponse)
  })
_sym_db.RegisterMessage(GetReportsByUserIdResponse)

UploadAudioRequest = _reflection.GeneratedProtocolMessageType('UploadAudioRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADAUDIOREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.UploadAudioRequest)
  })
_sym_db.RegisterMessage(UploadAudioRequest)

UploadAudioResponse = _reflection.GeneratedProtocolMessageType('UploadAudioResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADAUDIORESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.UploadAudioResponse)
  })
_sym_db.RegisterMessage(UploadAudioResponse)

StartAttemptRequest = _reflection.GeneratedProtocolMessageType('StartAttemptRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTATTEMPTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.StartAttemptRequest)
  })
_sym_db.RegisterMessage(StartAttemptRequest)

StartAttemptResponse = _reflection.GeneratedProtocolMessageType('StartAttemptResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTATTEMPTRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.StartAttemptResponse)
  })
_sym_db.RegisterMessage(StartAttemptResponse)

AttachReportToAttemptRequest = _reflection.GeneratedProtocolMessageType('AttachReportToAttemptRequest', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHREPORTTOATTEMPTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.AttachReportToAttemptRequest)
  })
_sym_db.RegisterMessage(AttachReportToAttemptRequest)

GetReportByAttemptRequest = _reflection.GeneratedProtocolMessageType('GetReportByAttemptRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTBYATTEMPTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetReportByAttemptRequest)
  })
_sym_db.RegisterMessage(GetReportByAttemptRequest)

GetReportByAttemptResponse = _reflection.GeneratedProtocolMessageType('GetReportByAttemptResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTBYATTEMPTRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetReportByAttemptResponse)
  })
_sym_db.RegisterMessage(GetReportByAttemptResponse)

GetAudiousInArchiveRequest = _reflection.GeneratedProtocolMessageType('GetAudiousInArchiveRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUDIOUSINARCHIVEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetAudiousInArchiveRequest)
  })
_sym_db.RegisterMessage(GetAudiousInArchiveRequest)

GetAudiousInArchiveResponse = _reflection.GeneratedProtocolMessageType('GetAudiousInArchiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAUDIOUSINARCHIVERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetAudiousInArchiveResponse)
  })
_sym_db.RegisterMessage(GetAudiousInArchiveResponse)



_STORAGE = _descriptor.ServiceDescriptor(
  name='Storage',
  full_name='protos.Storage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1018,
  serialized_end=1520,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetQuestions',
    full_name='protos.Storage.GetQuestions',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETQUESTIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartAttempt',
    full_name='protos.Storage.StartAttempt',
    index=1,
    containing_service=None,
    input_type=_STARTATTEMPTREQUEST,
    output_type=_STARTATTEMPTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadAudio',
    full_name='protos.Storage.UploadAudio',
    index=2,
    containing_service=None,
    input_type=_UPLOADAUDIOREQUEST,
    output_type=_UPLOADAUDIORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AttachReportToAttempt',
    full_name='protos.Storage.AttachReportToAttempt',
    index=3,
    containing_service=None,
    input_type=_ATTACHREPORTTOATTEMPTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetReportByAttempt',
    full_name='protos.Storage.GetReportByAttempt',
    index=4,
    containing_service=None,
    input_type=_GETREPORTBYATTEMPTREQUEST,
    output_type=_GETREPORTBYATTEMPTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAudiousInArchive',
    full_name='protos.Storage.GetAudiousInArchive',
    index=5,
    containing_service=None,
    input_type=_GETAUDIOUSINARCHIVEREQUEST,
    output_type=_GETAUDIOUSINARCHIVERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORAGE)

DESCRIPTOR.services_by_name['Storage'] = _STORAGE

# @@protoc_insertion_point(module_scope)