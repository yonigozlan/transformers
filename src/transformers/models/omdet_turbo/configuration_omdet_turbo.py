# coding=utf-8
# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""OmDet-Turbo model configuration"""

from ...configuration_utils import PretrainedConfig
from ...utils import logging
from ..auto import CONFIG_MAPPING


logger = logging.get_logger(__name__)


class OmDetTurboConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`OmDetTurboModel`]. It is used to instantiate a
    OmDet-Turbo model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the OmDet-Turbo
    [omlab/omdet-turbo-tiny](https://huggingface.co/omlab/omdet-turbo-tiny) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`PretrainedConfig`, *optional*):
            The configuration of the text model.
        vision_config (`PretrainedConfig`, *optional*):
            The configuration of the vision model.
        use_timm_backbone (`bool`, *optional*, defaults to `True`):
            Whether to use the timm backbone.
        backbone (`<fill_type>`, *optional*, defaults to `"swin_tiny_patch4_window7_224"`): <fill_docstring>
        backbone_kwargs (`dict`, *optional*):
            Additional kwargs for the backbone.
        backbone_out_indices (`<fill_type>`, *optional*, defaults to `[1, 2, 3]`): <fill_docstring>
        backbone_embed_dim (`<fill_type>`, *optional*, defaults to 96): <fill_docstring>
        backbone_qkv_bias (`<fill_type>`, *optional*, defaults to `True`): <fill_docstring>
        backbone_depths (`<fill_type>`, *optional*, defaults to `[2, 2, 6, 2]`): <fill_docstring>
        backbone_num_heads (`<fill_type>`, *optional*, defaults to `[3, 6, 12, 24]`): <fill_docstring>
        backbone_window_size (`<fill_type>`, *optional*, defaults to 7): <fill_docstring>
        backbone_features_only (`<fill_type>`, *optional*, defaults to `True`): <fill_docstring>
        use_pretrained_backbone (`<fill_type>`, *optional*, defaults to `True`): <fill_docstring>
        backbone_image_size (`<fill_type>`, *optional*, defaults to 640): <fill_docstring>
        encoder_hidden_dim (`int`, *optional*, defaults to 256):
            The hidden dimension of the encoder.
        decoder_hidden_dim (`int`, *optional*, defaults to 256):
            The hidden dimension of the decoder.
        backbone_feat_channels (`tuple(int)`, *optional*, defaults to `[256, 256, 256]`):
            The feature channels of the backbone.
        num_feature_levels (`int`, *optional*, defaults to 3):
            The number of feature levels.
        disable_custom_kernels (`bool`, *optional*, defaults to `False`):
            Whether to disable custom kernels.
        text_projection_in_features (`int`, *optional*, defaults to 512):
            The input features for the text projection.
        text_projection_out_features (`int`, *optional*, defaults to 512):
            The output features for the text projection.
        num_queries (`int`, *optional*, defaults to 900):
            The number of queries.
        layer_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon value for layer normalization.
        batch_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon value for batch normalization.
        csp_activation (`str`, *optional*, defaults to `"silu"`):
            The activation function of the Cross Stage Partial (CSP) networks of the encoder.
        conv_norm_activation (`str`, *optional*, defaults to `"gelu"`):
            The activation function of the ConvNormLayer layers of the encoder.
        ffn_encoder_activation (`str`, *optional*, defaults to `"relu"`):
            The activation function for the feedforward network of the encoder.
        hidden_expansion (`int`, *optional*, defaults to 1):
            The hidden expansion of the CSP networks.
        dropout (`float`, *optional*, defaults to 0.0):
            The dropout rate of the encoder.
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The activation dropout rate of the encoder ffn.
        encoder_in_channels (`list(int)`, *optional*, defaults to `[192, 384, 768]`):
            The input channels for the encoder.
        encoder_feat_strides (`list(int)`, *optional*, defaults to `[8, 16, 32]`):
            The feature strides for the encoder.
        encode_proj_layers (`list(int)`, *optional*, defaults to `[2]`):
            The projection layers for the encoder.
        encoder_attention_heads (`int`, *optional*, defaults to 8):
            The number of attention heads for the encoder.
        normalize_before (`bool`, *optional*, defaults to `False`):
            Whether to normalize before in the encoder.
        eval_size (`int`, *optional*):
            The evaluation size.
        encoder_layers (`int`, *optional*, defaults to 1):
            The number of layers in the encoder.
        positional_encoding_temperature (`int`, *optional*, defaults to 10000):
            The positional encoding temperature.
        encoder_dim_feedforward (`int`, *optional*, defaults to 2048):
            The feedforward dimension for the encoder.
        decoder_num_heads (`int`, *optional*, defaults to 8):
            The number of heads for the decoder.
        decoder_num_layers (`int`, *optional*, defaults to 6):
            The number of layers for the decoder.
        label_dim (`int`, *optional*, defaults to 512):
            The dimension of the label.
        class_distance_type (`str`, *optional*, defaults to `"cosine"`):
            The type of of distance to compare predicted classes to labels.
        decoder_activation (`str`, *optional*, defaults to `"relu"`):
            The activation function for the decoder.
        decoder_encoder_dim_feedforward (`<fill_type>`, *optional*, defaults to 1024): <fill_docstring>
        decoder_dim_feedforward (`int`, *optional*, defaults to 2048):
            The feedforward dimension for the decoder.
        decoder_num_points (`int`, *optional*, defaults to 4):
            The number of points for the decoder.
        decoder_dropout (`float`, *optional*, defaults to 0.0):
            The dropout rate for the decoder.
        decoder_eval_idx (`int`, *optional*, defaults to -1):
            The evaluation index for the decoder.
        learn_init_query (`bool`, *optional*, defaults to `False`):
            Whether to learn the initial query.
        fuse_type (`str`, *optional*, defaults to `"merged_attn"`):
            The type of fusion.
        cache_size (`<fill_type>`, *optional*, defaults to 100): <fill_docstring>
        is_encoder_decoder (`bool`, *optional*, defaults to `True`):
            Whether the model is used as an encoder-decoder model or not.
        kwargs (`Dict[str, Any]`, *optional*):
            Additional parameters from the architecture. The values in kwargs will be saved as part of the configuration
            and can be used to control the model outputs.

    Examples:

    ```python
    >>> from transformers import OmDetTurboConfig, OmDetTurboModel

    >>> # Initializing a OmDet-Turbo omlab/omdet-turbo-tiny style configuration
    >>> configuration = OmDetTurboConfig()

    >>> # Initializing a model (with random weights) from the omlab/omdet-turbo-tiny style configuration
    >>> model = OmDetTurboModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = "omdet-turbo"
    attribute_map = {
        "encoder_hidden_dim": "d_model",
        "encoder_feat_strides": "feat_strides",
        "num_attention_heads": "encoder_attention_heads",
    }

    def __init__(
        self,
        text_config=None,
        vision_config=None,
        use_timm_backbone=True,
        backbone="swin_tiny_patch4_window7_224",
        backbone_kwargs=None,
        backbone_out_indices=[1, 2, 3],
        backbone_embed_dim=96,
        backbone_qkv_bias=True,
        backbone_depths=[2, 2, 6, 2],
        backbone_num_heads=[3, 6, 12, 24],
        backbone_window_size=7,
        backbone_features_only=True,
        use_pretrained_backbone=True,
        backbone_image_size=640,
        encoder_hidden_dim=256,
        decoder_hidden_dim=256,
        backbone_feat_channels=[256, 256, 256],
        num_feature_levels=3,
        disable_custom_kernels=False,
        text_projection_in_features=512,
        text_projection_out_features=512,
        num_queries=900,
        layer_norm_eps=1e-5,
        batch_norm_eps=1e-5,
        csp_activation="silu",
        conv_norm_activation="gelu",
        ffn_encoder_activation="relu",
        hidden_expansion=1,
        dropout=0.0,
        activation_dropout=0.0,
        encoder_in_channels=[192, 384, 768],
        encoder_feat_strides=[8, 16, 32],
        encode_proj_layers=[2],
        encoder_attention_heads=8,
        normalize_before=False,
        eval_size=None,
        encoder_layers=1,
        positional_encoding_temperature=10000,
        encoder_dim_feedforward=2048,
        decoder_num_heads=8,
        decoder_num_layers=6,
        label_dim=512,
        class_distance_type="cosine",
        decoder_activation="relu",
        decoder_encoder_dim_feedforward=1024,
        decoder_dim_feedforward=2048,
        decoder_num_points=4,
        decoder_dropout=0.0,
        decoder_eval_idx=-1,
        learn_init_query=False,
        fuse_type="merged_attn",
        cache_size=100,
        is_encoder_decoder=True,
        **kwargs,
    ):
        if use_timm_backbone and backbone_kwargs is None:
            backbone_kwargs = {
                "features_only": backbone_features_only,
                "out_indices": backbone_out_indices,
                "qkv_bias": backbone_qkv_bias,
                "img_size": backbone_image_size,
            }
        elif vision_config is None:
            logger.info("`vision_config` is `None`. Initializing the config with the default `swin` vision config.")
            vision_config = CONFIG_MAPPING["swin"](
                window_size=backbone_window_size,
                image_size=backbone_image_size,
                embed_dim=backbone_embed_dim,
                depths=backbone_depths,
                num_heads=backbone_num_heads,
                qkv_bias=backbone_qkv_bias,
                output_hidden_states=True,
                out_indices=[],
            )
        elif isinstance(vision_config, dict):
            backbone_model_type = vision_config.pop("model_type")
            config_class = CONFIG_MAPPING[backbone_model_type]
            vision_config = config_class.from_dict(vision_config)

        if text_config is None:
            logger.info(
                "`text_config` is `None`. Initializing the config with the default `clip_text_model` text config."
            )
            text_config = CONFIG_MAPPING["clip_text_model"]()
        elif isinstance(text_config, dict):
            text_model_type = text_config.pop("model_type")
            config_class = CONFIG_MAPPING[text_model_type]
            text_config = config_class.from_dict(text_config)

        self.text_config = text_config
        self.vision_config = vision_config
        self.use_timm_backbone = use_timm_backbone
        self.backbone = backbone
        self.backbone_kwargs = backbone_kwargs
        self.backbone_out_indices = backbone_out_indices
        self.backbone_embed_dim = backbone_embed_dim
        self.backbone_depths = backbone_depths
        self.backbone_num_heads = backbone_num_heads
        self.backbone_window_size = backbone_window_size
        self.backbone_image_size = backbone_image_size
        self.use_pretrained_backbone = use_pretrained_backbone
        self.encoder_hidden_dim = encoder_hidden_dim
        self.decoder_hidden_dim = decoder_hidden_dim
        self.backbone_feat_channels = backbone_feat_channels
        self.num_feature_levels = num_feature_levels
        self.disable_custom_kernels = disable_custom_kernels
        self.text_projection_in_features = text_projection_in_features
        self.text_projection_out_features = text_projection_out_features
        self.num_queries = num_queries
        self.layer_norm_eps = layer_norm_eps
        self.batch_norm_eps = batch_norm_eps
        self.csp_activation = csp_activation
        self.conv_norm_activation = conv_norm_activation
        self.ffn_encoder_activation = ffn_encoder_activation
        self.hidden_expansion = hidden_expansion
        self.dropout = dropout
        self.activation_dropout = activation_dropout
        self.encoder_in_channels = encoder_in_channels
        self.encoder_feat_strides = encoder_feat_strides
        self.encode_proj_layers = encode_proj_layers
        self.encoder_attention_heads = encoder_attention_heads
        self.normalize_before = normalize_before
        self.eval_size = eval_size
        self.encoder_layers = encoder_layers
        self.positional_encoding_temperature = positional_encoding_temperature
        self.encoder_dim_feedforward = encoder_dim_feedforward
        self.decoder_num_heads = decoder_num_heads
        self.decoder_num_layers = decoder_num_layers
        self.label_dim = label_dim
        self.class_distance_type = class_distance_type
        self.decoder_activation = decoder_activation
        self.decoder_encoder_dim_feedforward = decoder_encoder_dim_feedforward
        self.decoder_dim_feedforward = decoder_dim_feedforward
        self.decoder_num_points = decoder_num_points
        self.decoder_dropout = decoder_dropout
        self.decoder_eval_idx = decoder_eval_idx
        self.learn_init_query = learn_init_query
        self.fuse_type = fuse_type
        self.cache_size = cache_size

        super().__init__(is_encoder_decoder=is_encoder_decoder, **kwargs)
