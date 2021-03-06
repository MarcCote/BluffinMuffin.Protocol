﻿using BluffinMuffin.Protocol.DataTypes.Enums;
using BluffinMuffin.Protocol.DataTypes.Options;

namespace BluffinMuffin.Protocol.DataTypes.Options
{
    /// <summary>
    /// With no blinds, the preflop round starts as avery other round, with no money on the Table.
    /// </summary>
    public class BlindOptionsNone : BlindOptions
    {
        /// <summary>
        /// 
        /// </summary>
        public override BlindTypeEnum OptionType { get { return BlindTypeEnum.None; } }
    }
}